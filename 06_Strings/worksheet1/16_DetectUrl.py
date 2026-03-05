"""
Detect URLs Within a String
Explanation: Extract all URLs from the string.
Input: "Check this link: https://openai.com and http://github.com"
Expected Output: URLs found: ['https://openai.com', 'http://github.com']"""
import re

text = "Check this link: https://openai.com and http://github.com"
pattern = r'https?://[^\s]+'
urls = re.findall(pattern, text)
print("URLs found:", urls)
