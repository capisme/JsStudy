import requests
import wanfang_pb2 as pb

# params = {
# currentPage: 1
# pageSize: 20
# searchFilter: [0]
# searchScope: 0
# searchSort: {__ob__: Mt}
# searchType: "paper"
# searchWord: "爬虫"
# }
# {"searchType":"paper","searchWord":"爬虫","currentPage":1,"pageSize":20,"searchFilter":[0],"searchSort":{"field":"","order":1},"searchScope":0}
searchRequest = pb.SearchService.SearchRequest()
# search_request = searchRequest.SearchService.commonRequest.add()

searchRequest.commonRequest.searchType = "paper"
searchRequest.commonRequest.searchWord = "java"
searchRequest.commonRequest.currentPage = 1
searchRequest.commonRequest.pageSize = 20
searchRequest.commonRequest.searchFilter.append(0)
searchSort = searchRequest.commonRequest.searchSort.add()
searchSort.B = " "
searchSort.C = 1
searchRequest.commonRequest.searchScope = 0

print(searchRequest)

'''万方数据网'''
import struct
import requests
import blackboxprotobuf

url = 'https://s.wanfangdata.com.cn/SearchService.SearchService/search?'

headers = {
    'origin': 'https://s.wanfangdata.com.cn',
    'Content-Type': 'application/grpc-web+proto',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    'x-grpc-web': '1',
    'x-user-agent': 'grpc-web-javascript/0.1'
}

# print(search_request)
bytes_body = searchRequest.SerializeToString()

bytes_head = bytes([0, 0, 0, 0, len(bytes_body)])

resp = requests.post(url=url, data=bytes_head + bytes_body, headers=headers)
# print(resp.text)
data_len = struct.unpack(">i", resp.content[1:5])[0]
print(data_len)

message, typedef = blackboxprotobuf.protobuf_to_json(resp.content[5:5 + data_len])
print(message)

with open("text1.bin", 'wb')as f:
    f.write(resp.content[5:5 + data_len])


with open(r"text1.bin", "rb") as fp:
    data = fp.read()
    message, typedef = blackboxprotobuf.protobuf_to_json(data)
    print(message)
