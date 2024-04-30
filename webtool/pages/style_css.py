content = f"""
/* created by script */
:root {{
    --global-warning-color: orange;
    --global-ok-color: #84b135;
    --global-error-color: #e43d2f;
    --global-header-color: #eee;
    --global-th-color: #0096a4;
}}


.border1 tr, .border1 td, .border1 th {{
    border: 1px solid black ;
    border-collapse: collapse;    

}}

.log-box {{
    grid-area: event-box;
    background-color: #f5f5f5;  
    min-height: 100px;
    max-height: 100px;
    overflow-y: auto;
    border: solid 1px;
}}


.data-state:disabled {{
    background-color: gray;
}}

.data-state[data-state="init"] {{
    background-color: var(--global-warning-color);
}}

.data-state[data-state="loading"] {{
    background-color: var(--global-warning-color);
    animation: pulse 1s infinite
}}

.data-state[data-state="done"] {{
    background-color: var(--global-ok-color);
}}

.data-state[data-state="none"] {{
    background-color: gray;
}}

.data-state[data-state="disabled"] {{
    background-color: gray;
}}

.data-state[data-state="error"] {{
    background-color: var(--global-error-color);
}}

.td[data-message] {{
    position: relative;
    text-decoration: underline;
    color: #00f;
    cursor: help;    
}}
"""