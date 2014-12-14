import praw
r = praw.Reddit(user_agent='startedfromtheBOTtom')

subreddit = r.get_subreddit('leagueoflegends')

# Number of top posts on this subreddit to search
TOP_POSTS_TO_SEARCH = 5

top_summoners = ['bjerg', 'Turtle the Cat', 'Pobelter', 'Doublelift', 'HotGuy6Pack','Apdo Dog', 'Crs KEITHMCBRIEF', 'WildTurtl']
tag_list = ['summoner']

unprocessed_comments = []
processed_comments = []

total_comments_searched = 0


class CommentToProcess():
    def __init__(self,comment, tags):
        self.body = comment.body.encode("utf-8")
        self.id = comment.id
        self.likes = comment.likes
        self.name = comment.name
        self.link_id = comment.link_id
        self.author = comment.author
        self.matching_tags = tags
        

    def __str__(self):
        temp =  'ID:'       + str(self.id) + '\n'
        temp += 'Author:'   + str(self.author) + '\n'
        temp += 'Name:'     + str(self.name) + '\n'
        temp += 'Linkid:'   + str(self.link_id) + '\n'
        temp += 'Likes:'    + str(self.likes) + '\n'
        temp += 'Tags:'     + str(self.matching_tags) + '\n'
        temp += 'Body:'     + str(self.body) + '\n'
        temp += '================================'
        return temp

    

# Search Reddit for new comments
def find_comments(): 
    submissions = subreddit.get_hot(limit=TOP_POSTS_TO_SEARCH)
    for submission in submissions:
        flat_comments = praw.helpers.flatten_tree(submission.comments);
        for comment in flat_comments:
            # Handle "praw.objects.MoreComments" instances
            if not isinstance(comment,praw.objects.Comment):
                continue
                
            # Check if this comment has the tag text
            matching_tags = []
            for tag in tag_list:
                if tag in comment.body:
                    matching_tags.append(tag)
            
            # Save comment if any tags match
            if len(matching_tags) > 0:
                newComment = CommentToProcess(comment, matching_tags)
                unprocessed_comments.append( newComment )
                    
                    
print "-------------------------------------"
print "Searching for comments matching tags: " + str(tag_list)
print "-------------------------------------"
find_comments()

for comment in unprocessed_comments:
    print comment
    
print "-------------------------------------"
print str(len(unprocessed_comments)) + " comments found matching."
print "-------------------------------------"

