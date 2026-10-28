from collections import Counter

from fastmcp import FastMCP
from prefab_ui.app import PrefabApp
from prefab_ui.components import Column, DataTable, DataTableColumn, Grid
from prefab_ui.components.charts import PieChart


mcp = FastMCP("My First FastMCP App")


@mcp.tool(app=True)
def team_directory() -> PrefabApp:
    """展示团队成员目录和办公地点分布。"""

    members = [
        {"name": "Alice Chen", "role": "Staff Engineer", "office": "San Francisco"},
        {"name": "Bob Martinez", "role": "Lead Designer", "office": "New York"},
        {"name": "Carol Johnson", "role": "Senior Engineer", "office": "London"},
        {"name": "David Kim", "role": "Product Manager", "office": "San Francisco"},
        {"name": "Eva Mueller", "role": "Engineer", "office": "Berlin"},
        {"name": "Frank Lee", "role": "Data Scientist", "office": "San Francisco"},
        {"name": "Grace Park", "role": "Engineering Manager", "office": "New York"}
    ]

    office_counts = [
        {"office": office, "count": count}
        for office, count in Counter(
            member["office"] for member in members
        ).items()
    ]

    with PrefabApp() as app:
        with Column(gap=4, css_class="p-6"):
            with Grid(columns=[1, 2], gap=4):
                PieChart(
                    data=office_counts,
                    data_key="count",
                    name_key="office",
                    show_legend=True
                )

                DataTable(
                    columns=[
                        DataTableColumn(
                            key="name",
                            header="Name",
                            sortable=True
                        ),
                        DataTableColumn(
                            key="role",
                            header="Role",
                            sortable=True
                        ),
                        DataTableColumn(
                            key="office",
                            header="Office",
                            sortable=True
                        )
                    ],
                    rows=members,
                    search=True
                )

    return app
