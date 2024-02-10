# ArXiv Retriever

# libraries
import os
from tavily import TavilyClient
from langchain.retrievers import ArxivRetriever


class arXivSearch():
    """
    arXiv API Retriever
    """
    def __init__(self, query):
        """
        Initializes the TavilySearch object
        Args:
            query:
        """
        self.query = query
        self.api_key = self.get_api_key()
        self.client = TavilyClient(self.api_key)

    def get_api_key(self):
        """
        Gets the Tavily API key
        Returns:

        """
        # Get the API key
        try:
            api_key = os.environ["TAVILY_API_KEY"]
        except:
            raise Exception("Tavily API key not found. Please set the TAVILY_API_KEY environment variable. "
                            "You can get a key at https://app.tavily.com")
        return api_key

    def search(self, max_results=7):
        """
        Searches the query direct on arXiv
        Returns: title, arXiv url, abstract part

        """
        #try:
        # Search the query
        print("Searching arXiv with query {0}...".format(self.query))
        retriever = ArxivRetriever(load_max_docs=max_results)
        docs = retriever.get_relevant_documents(query=self.query)

        #search_response = [{"href": obj["url"], "body": obj["content"]} for obj in results.get("results", [])]

        search_results = []
        # Normalizing results to match the format of the other search APIs
        for result in docs:
            search_result = {
                "title": result.metadata['Title'],
                "href": result.metadata['Entry ID'],
                "body": result.page_content,
            }
            search_results.append(search_result)
        return search_results

        #except Exception as e: # Fallback in case overload on Tavily Search API
        #    ddg = DDGS()
        #    search_response = ddg.text(self.query, region='wt-wt', max_results=max_results)
        #return search_response



