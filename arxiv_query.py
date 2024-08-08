import arxiv
import pandas as pd

# The query searches the abstract for the keyword groups
query = (
    "abs:(specular OR transparent OR reflective OR glass OR mirror) AND "
    "abs:(detection OR identification OR recognition OR localization) AND "
    "abs:(lidar OR \"light detection and ranging\" OR \"laser sensor\")"
)

# Execute query
search = arxiv.Search(
  query = query,
  max_results = 100,
  sort_by = arxiv.SortCriterion.SubmittedDate
)

# Quick solution for transforming the query into a pandas df and then excel sheet
arxiv_dict = {
    "Title": [],
    "Abstract": [],
    "Published": [],
    "Updated": []
}

for result in arxiv.Client().results(search):
    arxiv_dict["Title"].append(result.title)
    arxiv_dict["Abstract"].append(result.summary)
    arxiv_dict["Published"].append(result.published.strftime("%m/%d/%Y"))
    arxiv_dict["Updated"].append(result.updated.strftime("%m/%d/%Y"))

df = pd.DataFrame(data=arxiv_dict)
df.to_excel("out/arxiv.xlsx")
