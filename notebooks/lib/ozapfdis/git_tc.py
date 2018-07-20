import pandas as pd
import git
from io import StringIO


def log_numstat(path_to_git_repo):

	meta_data_format_string = "%x09%x09%x09%h%x09%aI%x09%aN"

	# connect to repo
	git_bin = git.Repo(path_to_git_repo).git

	# execute log command
	git_log = git_bin.execute('git log --no-merges --no-renames --numstat --pretty=format:"' + meta_data_format_string + '"')

	# read in the log
	git_log = pd.read_csv(
		StringIO(git_log), 
		sep="\t", 
		header=None,
		names=['additions', 'deletions', 'file', 'sha', 'timestamp', 'author']
	)

	# convert to DataFrame
	commit_data = git_log[['additions', 'deletions', 'file']]\
		.join(git_log[['sha', 'timestamp', 'author']]\
		.fillna(method='ffill'))\
		.dropna()
	
	files = pd.read_csv(StringIO(git_bin.execute('git ls-files')), 
		sep="\n", 
		header=None,
		names=['file'])
		
	commits = commit_data[commit_data['file'].isin(files['file'])].copy()
	commits['timestamp'] = pd.to_datetime(commits['timestamp'])
	return commits