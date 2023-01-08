questions = """
I'm learning elastic for a new project. I have a index with format:

{
    "content_id": "bbbbbb",
    "title": "content 2",
    "data": [
            {
              "id": "xx",
              "value": 3,
              "tags": ["a","b","c"]
            },
            {
              "id": "yy",
              "value": 1,
              "tags": ["e","d","c"]
            }
   ]
}
How can i make a query to search contents that have at least one element in data that include tags "a" and "b" ?

thanks so much !!

How can i make query or re design my format data to easy make new query ?
"""

answers = """
Working with lists and nested documents in Elasticsearch is a bit tricky.
When creating the index, you need to specify the mapping for the nested documents. You can do this by adding a mapping for the data field, this is the link to the documentation: https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-create-index.html#mappings

PUT /my_index

{
    "mappings": {
        "doc": {
            "properties": {
                "data": {
                    "type": "nested"
                }
            }
        }
    }
}


If you have already created the index, you should delete it first, then create it again with the mapping.

Before deleting the index, you can reindex (copy) the data to a new index.


Now you can query the data field using the nested query:

GET /my_index/_search

{
    "query": {
        "nested": {
            "path": "data",
            "query": {
                "terms": {
                    "data.tags": [
                        "j",
                        "b",
                        "c"
                    ]
                }
            }
        }
    }
}


"""



c1 = """

what is "doc" in mappings, can I ignore it ?

@quang-lê It is the `type` of the document. You can use any name you want. I think it has been removed in the latest version of Elasticsearch.
"""