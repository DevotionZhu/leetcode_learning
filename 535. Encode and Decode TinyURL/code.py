class Codec:
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        tiny_loader = str(hash(longUrl))
        self.table = {tiny_loader: longUrl}
        return "http://tinyurl.com/" + tiny_loader

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        _, tiny_loader = shortUrl.split("http://tinyurl.com/")
        return self.table[tiny_loader]


        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.decode(codec.encode(url))