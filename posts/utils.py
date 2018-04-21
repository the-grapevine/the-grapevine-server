import random
import string


def generate_post_key():
    """
    For now just generate a key. In the future we might use
    the hash of the post.
    For instance we could pass in the details of the post and hash then with a
    nonce to get a unique post has instead of a key...
    """
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase +
        string.digits + string.ascii_lowercase) for _ in range(32))
