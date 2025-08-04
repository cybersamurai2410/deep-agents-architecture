from langgraph.prebuilt.chat_agent_executor import AgentState
from typing import NotRequired, Annotated
from typing import Literal
from typing_extensions import TypedDict


class Todo(TypedDict):
    """Todo to track."""

    content: str
    status: Literal["pending", "in_progress", "completed"]

# Reducer merges file content; l and r are different dictionary states updated by the same agent.
def file_reducer(l, r):
    if l is None:
        return r
    elif r is None:
        return l
    else:
        return {**l, **r}


class DeepAgentState(AgentState):
    todos: NotRequired[list[Todo]] # List of todo tasks to track.
    files: Annotated[NotRequired[dict[str, str]], file_reducer] # Uses dict containing file content, not actual file system stored in disk.


"""
Example of a state during runtime:
{
  "messages": [...],                          # required (from AgentState)
  "remaining_steps": ...,                     # optional (from AgentState)
  "todos": [                                  # optional (from DeepAgentState)
    {"content": "do x", "status": "pending"},
    {"content": "do y", "status": "completed"}
  ],
  "files": {                                  # optional (from DeepAgentState)
    "report.md": "# My Report",
    "data.txt": "12345"
  }
}
"""
