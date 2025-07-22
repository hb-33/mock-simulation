
#Read the system.log file and identify the issue

import argparse
def mock_issue(fileName):
    issue_list = []
    with open(fileName, "r") as f:
        for line in f:
            if "ERROR" in line:
                issue_list.append(line)
    
    print(issue_list)




def main():
    parser = argparse.ArgumentParser(description="Mock simulation task")
    parser.add_argument("fileName", help="Enter the name of the file that has issue")
    args = parser.parse_args()
    mock_issue(args.fileName)




if __name__ == "__main__":
    main()