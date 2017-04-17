from facepy import GraphAPI
from urllib.request import urlopen


# initialising your access token
token = input("ENTER YOUR ACCESS TOKEN: ")
graph = GraphAPI(token)

# to post a status or photo 
def post():
    p_action = input('Message(m) or Photo(p): ')
    if p_action == 'm':
        path = 'me/feed'
        message = input("Enter Message: ")
        graph.post(path, message= message)
    elif p_action == 'p':
        path = 'me/photos'
        source = input("Enter photo name: ")
        graph.post(path,
                   source = open(source,'rb'))
    else:
        print('Wrong action')

def get():
    # Get my latest posts
    posts = graph.get('me/feed')
    posts = [x['id'] for x in posts['data']]

    return posts

# to search facebook
def search():
    term = input("ENTER YOUR SEARCH TERM: ")
    type = input("ENTER WHAT YOU WANT TO SEARCH(user,page,event,group,place,checkin): ")
    # Supported types are ``post``, ``user``, ``page``, ``event``, ``group``, ``place`` and ``checkin``.
    result = graph.search(term, type)
    for id in result['data']:
        print('result: ', id)

# to delete posts
def delete():
    p = get()
    for i in p:
        d = i
        try:
            print(d, ' deleting')
            o = input("ARE YOU SURE YOU WANT TO DELETE THIS FILE:(y/n): ")
            if o == 'y':
                graph.delete(d)
                print('Success','\n')
        except:
            print('not done! posts which are made using graph api can only be deleted')
            print('For using this first post something using post method in this app and then try delete','\n')
            continue

def action():
    """
     USE P TO POST INTO YOUR FACEBOOK ACCOUNT
     USE G TO GET DETAILS 
     USE S TO SEARCH IN FACEBOOK
     USE D TO DELETE AN ITEM
    """
    useraction = input("WHAT DO YOU WANT TO DO: ")
    if useraction == 'p':
        post()
    elif useraction == 'g':
        p = get()
        for i in p:
            print(i)
    elif useraction == 's':
        search()
    elif useraction == 'd':
        delete()
    else:
        print('unknown action')


action()
