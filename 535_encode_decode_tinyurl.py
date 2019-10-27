from collections import defaultdict
class Codec:
    
    def __init__(self):
        self.hash = string.ascii_lowercase + '0123456789'
        self.long2short = defaultdict(int)
        self.short2long = defaultdict(int)
    
    def makehash(self, url):
        newhash = ""
        while len(newhash)!= 6:
            newhash += random.choice(self.hash)
        return newhash

    def encode(self, longUrl):
        if longUrl in self.long2short:
            return self.long2short[longUrl]
        else:
            while (1):
                newhash = self.makehash(longUrl)
                if not 'http://tinyurl.com/+newhash' in self.short2long:
                    self.long2short[longUrl] = 'http://tinyurl.com/+newhash' 
                    self.short2long['http://tinyurl.com/+newhash' ] = longUrl
                    return 'http://tinyurl.com/+newhash'               
        
        

    def decode(self, shortUrl):
        return self.short2long[shortUrl]
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
