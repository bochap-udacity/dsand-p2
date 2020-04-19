# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, path, absolute_path):
        # Insert the node as before
        if path not in self.children:
            self.children[path] = RouteTrieNode(absolute_path)
        return self.children[path]


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler, not_found_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler)
        self.not_found = RouteTrieNode(not_found_handler)

    def insert(self, paths, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_path = self.root
        for index in range(len(paths)):
            current_path = current_path.insert(
                paths[index], None if index < len(paths) - 1 else handler
            )

    def find(self, paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if len(paths) == 0:
            return self.root.handler

        current_path = self.root
        for index in range(len(paths)):
            path = paths[index]
            if path not in current_path.children:
                return self.not_found.handler

            current_path = current_path.children[path]

        return (
            current_path.handler
            if current_path.handler != None
            else self.not_found.handler
        )


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie(root_handler, not_found_handler)

    def add_handler(self, absolute_path, path_handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        paths = self.split_path(absolute_path)
        self.router.insert(paths, path_handler)

    def lookup(self, absolute_path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        paths = self.split_path(absolute_path)
        return self.router.find(paths)

    def split_path(self, absolute_path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return [
            path for path in absolute_path.split("/") if path != None and len(path) > 0
        ]


# Here are some test cases and expected outputs you can use to test your implementation
def testRouter():
    # create the router and add a route
    router = Router(
        "root handler", "not found handler"
    )  # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route

    assert router.lookup("") == "root handler"
    print(router.lookup(""))  # should print 'root handler'

    assert router.lookup("/") == "root handler"
    print(router.lookup("/"))  # should print 'root handler'
    assert router.lookup("/home") == "not found handler"
    print(
        router.lookup("/home")
    )  # should print 'not found handler' or None if you did not implement one
    assert router.lookup("/home/about") == "about handler"
    print(router.lookup("/home/about"))  # should print 'about handler'
    assert router.lookup("/home/about/") == "about handler"
    print(
        router.lookup("/home/about/")
    )  # should print 'about handler' or None if you did not handle trailing slashes
    print(
        router.lookup("/home/about/me")
    )  # should print 'not found handler' or None if you did not implement one
    print("router testing completed")


testRouter()
