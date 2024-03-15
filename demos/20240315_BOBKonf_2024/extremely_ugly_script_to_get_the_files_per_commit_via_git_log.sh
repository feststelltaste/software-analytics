#!/bin/bash

# Define the repository directory
REPO_DIR="../../angular/"

# Move to the repository directory
cd "$REPO_DIR" || exit

# Print CSV header as first line
echo "sha,timestamp,action,file_path"

# create variables for the repeated information per file
commit_hash=""
commit_timestamp=""

# Git log all the things and iterate through each commit
git log --pretty=format:"INFO,%H,%at" --date=format:"%Y-%m-%d %H:%M:%S" --name-status --diff-filter=ADR -- '*.ts' '*.js' | while read -r line; do
	
	if [[ "$line" =~ "INFO" ]]; then
		commit_hash=$(echo "$line" | cut -d ',' -f 2)
		commit_timestamp=$(echo "$line" | cut -d ',' -f 3)	
	fi

    # Check if the line contains actions for add and delete
	if [[ "$line" =~ ^[AD] ]]; then
	
        action=$(echo "$line" | cut -d$'\t' -f 1)
        file_path=$(echo "$line" | cut -d$'\t' -f 2)
		
        # Print commit information in CSV format
        echo "$commit_hash,$commit_timestamp,$action,$file_path"
	fi
	
	# Treat rename as add and delete action
	if [[ "$line" =~ ^[R] ]]; then
	
        action="D"
        file_path=$(echo "$line" | cut -d$'\t' -f 2)
		
		echo "$commit_hash,$commit_timestamp,$action,$file_path"
		
		action="A"
        file_path=$(echo "$line" | cut -d$'\t' -f 3)
		
        echo "$commit_hash,$commit_timestamp,$action,$file_path"
	fi
done
