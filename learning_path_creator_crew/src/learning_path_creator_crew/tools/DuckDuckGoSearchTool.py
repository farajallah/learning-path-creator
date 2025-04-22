from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_community.tools import DuckDuckGoSearchResults


class DuckDuckGoSearchTool(BaseModel):
    """Input schema for DuckDuckGoSearchTool."""
    search_query: str = Field(..., description="Description of the search_query.")

class DuckDuckGoSearchTool(BaseTool):
    verbose: bool = False # Optional; set to True for verbose output.
    def __init__(self, verbose=False, **kwargs):
        super().__init__(**kwargs)
        self.verbose = verbose
    
    name: str = "DuckDuckGo Search"
    description: str = "A tool that uses DuckDuckGo to search the web for relevant information based on a query."
    args_schema: Type[BaseModel] = DuckDuckGoSearchTool
    

    def _run(self, search_query: str) -> str:
        if self.verbose:
            print(f"\n>> DuckDuckGo Searching: {search_query}\n")

        try:
            # Fetch more results to give the assessor agent more context
            search = DuckDuckGoSearchResults(output_format="list")
            results = search.invoke(search_query, max_results=10)

            if results:
                return "\n".join([f"- Title: {r['title']}\n  URL: {r['link']}\n  Snippet: {r['snippet']}" for r in results])
            else:
                return "No relevant results found."
        except Exception as e:
             print(f"Error during DuckDuckGo search: {e}")
             return f"Error performing search: {e}"
