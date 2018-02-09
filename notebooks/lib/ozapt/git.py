import pandas as pd
import git
from io import StringIO


def retrieve_file_statistics(path_to_git_repo, meta_data_list):

	meta_data_format_string = "%x09".join(meta_data_list)

	# connect to repo
	git_bin = git.Repo(path_to_git_repo).git

	# execute log command
	git_log = git_bin.execute('git log --no-merges --no-renames --numstat --pretty=format:"%x09%x09%x09' + meta_data_format_string + '"')

	# read in the log
	git_log = pd.read_csv(
		StringIO(git_log), 
		sep="\t", 
		header=None,
		names=['additions', 'deletions', 'path','author']
	)

	# convert to DataFrame
	commit_data = git_log[['additions', 'deletions', 'path']]\
		.join(git_log[['author']]\
		.fillna(method='ffill'))\
		.dropna()
		
	return commit_data