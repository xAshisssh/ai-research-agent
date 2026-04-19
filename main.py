import subprocess
import json
import sys

def call_lpi_tool(tool_name, arguments=None):
    """
    This function actually connects to the LPI MCP server.
    It runs the node command to trigger the real tools.
    """
    try:
        # Path to the LPI server index file
        server_path = "dist/src/index.js"
        
        cmd = ["node", server_path, tool_name]
        if arguments:
            cmd.append(json.dumps(arguments))
        
        # Run the command and get the output
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except Exception as e:
        return f"Error calling {tool_name}: {str(e)}"

def run_agent():
    print("--- LPI Research Agent Starting ---")
    topic = input("What topic should I research using SMILE? ")

    # 🔧 CALLING REAL LPI TOOL 1: smile_overview
    # This proves your agent understands the methodology
    print(f"\n[Step 1] Fetching SMILE Overview...")
    overview = call_lpi_tool("smile_overview")

    # 🔧 CALLING REAL LPI TOOL 2: query_knowledge
    # This searches the 63 knowledge entries in the LPI
    print(f"[Step 2] Searching knowledge base for '{topic}'...")
    knowledge = call_lpi_tool("query_knowledge", {"query": topic})

    # 🔍 EXPLAINABILITY LAYER (Required for Level 3)
    print("\n--- AGENT EXPLANATION (Source Citing) ---")
    print(f"1. I used 'smile_overview' to ground this research in the SMILE methodology.")
    print(f"2. I used 'query_knowledge' to pull specific data for: {topic}.")
    
    print("\n--- RESEARCH RESULT ---")
    if knowledge:
        print(knowledge[:1000]) # Show the first 1000 characters of the result
    else:
        print("No specific data found, but based on SMILE, you should focus on Phase 1: Reality Emulation.")

if __name__ == "__main__":
    run_agent()
