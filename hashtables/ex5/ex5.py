# pass



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    result = []
    path_dict = {}

    for i in files:
        splits = i.split("/")
        file_names = splits.pop()
        paths = "/".join(splits)

        if file_names in path_dict.keys():
            path_dict[file_names].append(paths)

        else:
            path_dict[file_names] = [paths]
    
    for query in queries:
        if query in path_dict.keys():
            for path in path_dict[query]:
                files_found = (path + "/" + query)
                result.append(files_found)
            else:
                continue








    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
