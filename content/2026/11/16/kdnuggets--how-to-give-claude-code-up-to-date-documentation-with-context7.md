---
title: How to Give Claude Code Up-to-Date Documentation With Context7 - KDnuggets
source_url: https://www.kdnuggets.com/how-to-give-claude-code-up-to-date-documentation-with-context7
source_site: KDnuggets
source_slug: kdnuggets
description: Stop wasting tokens debugging outdated code. Give Claude Code up-to-date
  docs with Context7.
image: https://www.kdnuggets.com/wp-content/uploads/kdn-how-to-give-claude-code-up-to-date-documentation-with-context7-feature.webp
published: '2026-11-16T00:00:00Z'
scraped_at: '2026-11-17T03:47:12Z'
categories:
- Technology & Software
- Science
people:
- Claude Code
- Kanwal Mehreen
locations:
- Claude Code
organisations:
- APAC
- Claude Code
- Context7
- FEMCodes
- Harvard WeCode Scholar
- MCP
- Mitacs Globalink Research Scholar
- Proxy
- Teradata Diversity
---

# How to Give Claude Code Up-to-Date Documentation With Context7

Stop wasting tokens debugging outdated code. Give Claude Code up-to-date docs with Context7.

![How to Give Claude Code Up-to-Date Documentation With Context7](https://www.kdnuggets.com/wp-content/uploads/kdn-how-to-give-claude-code-up-to-date-documentation-with-context7-feature.webp)

If you do vibe coding, have you ever run into this issue? You ask **Claude Code** to build an AI application, and it generates the code using a library version that is incompatible with your project. For example, you have**LangChain** 1.x installed, but Claude Code generates code from an older tutorial that uses

```
LLMChain
```

:

```
```
from langchain.chains import LLMChain
```
```

You run the application and get an import error because this older API is not available in your installed setup. Now Claude Code has to investigate the version mismatch, look for the updated API, rewrite the code, and try again. Depending on the issue, it might take several attempts before everything works. There is no doubt that Claude Code can generate entire applications for you. The problem is that the frameworks and libraries it relies on keep changing, and Claude's built-in knowledge does not always reflect these changes. These failed runs are not just frustrating. They also cost time and tokens.

One way to address this is **Context7**, an open-source Model Context Protocol (MCP) server developed by** Upstash** that lets AI coding agents retrieve version-specific library documentation and code examples while working on a project. So, instead of manually searching documentation and pasting examples into Claude Code, you can connect Context7 and let the agent retrieve relevant information while working on your project.

In this tutorial, we will explore how Context7 works, connect it to Claude Code, configure automatic documentation retrieval, and test it with some examples. So, let's get started.

## What Is Context7 and How Does It Work?

Context7 is a documentation retrieval service that integrates with AI coding assistants through two main MCP tools:

```
resolve-library-id
```

, which identifies the correct library, and

```
query-docs
```

, which retrieves documentation related to a specific question. Whatever it returns acts as additional context before Claude writes the implementation.

Context7 also has several benefits, including:

* **Current documentation:** Retrieve relevant framework and library references instead of relying entirely on the model's built-in knowledge
* **Version-specific examples:** Find documentation for supported library versions
* **Fewer outdated APIs:** Reduce the chances of generating code using deprecated functions
* **MCP integration:** Connect documentation retrieval directly to Claude Code and other compatible coding assistants
* **Less manual work:** Avoid repeatedly searching documentation websites and copying examples into your prompts

Now, let us set it up with Claude Code.

## Step 1: Installing Context7 for Claude Code

Before getting started, make sure you have Claude Code installed and working. You can check your Claude Code installation by opening a terminal and running:

```
```
claude --version
```
```

For the recommended Context7 command-line interface (CLI) installation, you also need **Node.js** 22.13 or newer. You can check your versions with:

```
```
node --version
npm --version
```
```

If both commands return version information and Node.js meets the minimum requirement, you are ready.

Now install and configure Context7 using a single command:

```
```
npx ctx7 setup --claude
```
```

This command launches an interactive setup that allows you to configure Context7 specifically for Claude Code. You will be asked to authenticate with Context7 and select an integration mode. There are two options:

* **MCP server:** Connects Claude Code to Context7 through MCP tools
* **CLI + Skills:** Installs a skill that teaches Claude Code to retrieve documentation using Context7 CLI commands

For this tutorial, select the MCP option because it allows us to examine how Claude Code interacts with Context7's documentation tools. The setup process authenticates your account, creates an API key, and configures the necessary integration. It also installs instructions that help Claude Code recognize when documentation retrieval is needed. When everything is set up, you will see something like this at the end:

```
```
  Press Enter to open the browser, or Ctrl-C to quit...
  ✔ Authenticated with API key

✔ Context7 setup complete

  Claude Code
    + MCP server configured with API Key
    + Rule installed
    + Skill installed
```
```

## Step 2: Verifying the Context7 Connection

After completing the setup, open Claude Code:

```
```
claude
```
```

Inside Claude Code, enter:

```
```
/mcp
```
```

This opens the MCP management interface, where you can inspect the available servers and their connection status. Look for Context7 and check that it is connected.

```
```
Output:
Context7 MCP Server

Status:       ✔ connected
Auth:         ✔ authenticated
URL:          [https://mcp.context7.com/mcp](https://mcp.context7.com/mcp)
Capabilities: tools
```
```

You can also inspect configured MCP servers directly from your terminal using this command:

```
```
claude mcp list
```
```

If the MCP connection is working, Claude Code should be able to access the two Context7 tools:

```
resolve-library-id
```

and

```
query-docs
```

. If Context7 is missing or disconnected, restart Claude Code, check your authentication, and repeat the setup if necessary.

## Step 3: Testing Context7 With a Coding Task

Now we can test whether Claude Code can retrieve documentation before generating code.

For this example, we will use **Next.js** 16.

Start Claude Code inside an existing Next.js project, or create a new project and open Claude Code there.

Enter the following prompt:

```
```
Use Context7 to retrieve the Next.js 16 documentation for the proxy convention. Show me how to protect a dashboard route by checking an authentication cookie and redirecting unauthenticated users to `/login`. Explain which Next.js APIs are required, and implement the solution using the current documentation.
```
```

Here is what happens:

* Claude Code recognizes that your request requires Next.js documentation
* Context7 resolves the correct Next.js library, if necessary
* The agent retrieves relevant documentation about the proxy convention
* Claude Code uses the retrieved examples to generate or modify the project's code

Here is what Claude Code returned in our run. In the terminal, you can see that it called Context7 four times and named the documentation version it used:

```
```
Called context7 4 times

Sources: the Next.js docs on Context7 (/vercel/next.js/v16.2.9), specifically the
proxy file convention, the Proxy getting-started guide, the authentication guide,
the redirecting guide and the v16 upgrade guide.
```
```

It then summarized what changed in Next.js 16:

* ```
  middleware.ts
  ```

  is now

  ```
  proxy.ts
  ```

  . The old file name and the

  ```
  middleware
  ```

  named export are deprecated. Export a function called

  ```
  proxy
  ```

  instead (a default export also works).
* File location. Put

  ```
  proxy.ts
  ```

  in the project root, or in

  ```
  src/
  ```

  , at the same level as

  ```
  app/
  ```

  or

  ```
  pages/
  ```

  .
* Runtime. Proxy always runs on Node.js and can't use the edge runtime. If you need edge, the docs say to keep using

  ```
  middleware
  ```

  .
* Migrating.

  ```
  npx @next/codemod@canary middleware-to-proxy .
  ```

  renames the file and the function for you.

It also listed the APIs required for the solution:

| API | From | Purpose |
| --- | --- | --- |
| ``` proxy(request) ```  export | ``` proxy.ts ``` | Runs on the server before a matched request completes |
| ``` NextRequest ```  (type) | ``` next/server ``` | The incoming request;  ``` request.cookies.get(name) ```  reads a cookie and  ``` request.nextUrl.pathname ```  gives the path |
| ``` NextResponse.redirect(url) ``` | ``` next/server ``` | Sends the redirect; the URL must be absolute, so use  ``` new URL('/login', request.url) ``` |
| ``` NextResponse.next() ``` | ``` next/server ``` | Lets the request continue |
| ``` export const config = { matcher } ``` | ``` proxy.ts ``` | Limits which paths proxy runs on. Without it, proxy runs on every request, including static files and images |

Finally, it added the code. The important part of this experiment is not just the generated code. It is whether Claude Code actually used the documentation tools and selected APIs appropriate for your project. You can ask Claude to explain which documentation it retrieved and why it selected a particular implementation.

## Step 4: Making Context7 Work Automatically

One of the biggest advantages of Context7 is that you do not need to explicitly request documentation every time. The recommended setup installs a skill intended to activate when Claude Code encounters library-related questions.

However, if you are using a manual MCP installation, or want more explicit control, you can configure a rule using

```
CLAUDE.md
```

.

Claude Code reads this file to understand project instructions and development preferences.

Open the file in your project directory:

```
```
nano CLAUDE.md
```
```

Add the following rule:

```
```
## Library Documentation

Always use Context7 when working with external libraries,
frameworks, or APIs.

Before generating code:
1. Identify the library and its installed version.
2. Retrieve relevant documentation using Context7.
3. Prefer examples matching the project's version.
4. Avoid deprecated APIs when supported alternatives exist.
5. Check the generated code against the documentation.
```
```

Save the file.

Now, when you ask Claude Code to create a feature involving a supported framework or API, it has an explicit instruction to consult Context7 before implementing it.

For example, you can simply write:

```
```
Add Supabase email and password authentication to my application.
```
```

Claude Code can use the Context7 integration without you adding the phrase

```
use context7
```

. If you want the rule to apply across all your projects, you can place it in your user-level Claude Code instructions:

```
```
nano ~/.claude/CLAUDE.md
```
```

## Step 5: Using Context7 With Specific Library Versions

Another useful Context7 feature is the ability to request documentation for a specific library version. This matters when working with applications that have not yet migrated to the latest release.

For example:

```
```
Using Context7, retrieve the documentation for Pydantic v2 and show how to migrate a BaseModel from Pydantic v1.
```
```

Claude Code called Context7 four times and used the **Pydantic** v2 documentation (

```
/pydantic/pydantic/v2.14.1
```

), specifically the migration guide and the validators and models concept pages.

Here is the Pydantic v1 model it started from:

```
```
from typing import Optional, List
from pydantic import BaseModel, Field, validator, root_validator

class User(BaseModel):
    id: int
    username: str
    nickname: Optional[str]              # v1: optional, defaults to None
    tags: List[str] = []
    password: str
    password_repeat: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        anystr_strip_whitespace = True
        schema_extra = {"example": {"id": 1, "username": "kanwal"}}

    @validator("username")
    def username_alphanumeric(cls, v):
        assert v.isalnum(), "must be alphanumeric"
        return v

    @validator("tags", each_item=True)
    def tag_not_empty(cls, v):
        assert v, "empty tag"
        return v

    @root_validator(skip_on_failure=True)
    def passwords_match(cls, values):
        if values.get("password") != values.get("password_repeat"):
            raise ValueError("Passwords do not match")
        return values

user = User.parse_obj(data)
user.dict(); user.json(); user.copy()
User.from_orm(orm_obj)
```
```

And here is the same model after the migration to Pydantic v2:

```
```
from typing import Annotated, Optional
from typing_extensions import Self
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

class User(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,          # was orm_mode
        populate_by_name=True,         # was allow_population_by_field_name
        str_strip_whitespace=True,     # was anystr_strip_whitespace
        json_schema_extra={"example": {"id": 1, "username": "kanwal"}},  # was schema_extra
    )

    id: int
    username: str
    nickname: Optional[str] = None     # explicitly optional
    tags: list[Annotated[str, Field(min_length=1)]] = []   # replaces each_item=True
    password: str
    password_repeat: str

    @field_validator("username")
    @classmethod
    def username_alphanumeric(cls, v: str) -> str:
        if not v.isalnum():
            raise ValueError("must be alphanumeric")
        return v

    @model_validator(mode="after")
    def passwords_match(self) -> Self:
        if self.password != self.password_repeat:
            raise ValueError("Passwords do not match")
        return self

user = User.model_validate(data)
user.model_dump(); user.model_dump_json(); user.model_copy()
User.model_validate(orm_obj)            # replaces from_orm (needs from_attributes=True)
```
```

It also explained what changed, step by step. First,

```
class Config
```

becomes

```
model_config = ConfigDict(...)
```

. The inner

```
Config
```

class is deprecated, and several settings were renamed:

| v1 | v2 |
| --- | --- |
| ``` orm_mode ``` | ``` from_attributes ``` |
| ``` allow_population_by_field_name ``` | ``` populate_by_name ```  (or  ``` validate_by_name ```  from v2.11) |
| ``` anystr_strip_whitespace ```  /  ``` anystr_lower ```  /  ``` anystr_upper ``` | ``` str_strip_whitespace ```  /  ``` str_to_lower ```  /  ``` str_to_upper ``` |
| ``` min_anystr_length ```  /  ``` max_anystr_length ``` | ``` str_min_length ```  /  ``` str_max_length ``` |
| ``` schema_extra ``` | ``` json_schema_extra ``` |
| ``` validate_all ``` | ``` validate_default ``` |
| ``` keep_untouched ``` | ``` ignored_types ``` |

Second, the methods on

```
BaseModel
```

were renamed. The old names still work but raise deprecation warnings. Third,

```
@validator
```

becomes

```
@field_validator
```

. Fourth,

```
@root_validator
```

becomes

```
@model_validator
```

. Lastly,

```
Optional[T]
```

no longer implies a default, which is a breaking change. In v2,

```
Optional[str]
```

with no default is required but accepts

```
None
```

. To keep the v1 behavior, write

```
Optional[str] = None
```

. This causes some of the most unexpected "Field required" errors after upgrading.

Providing the library ID saves the agent from performing an additional library-resolution step.

Context7 can match version-specific documentation when it is available in its index, but you should still verify that the returned material corresponds to the requested version.

## Step 6: Installing Context7 as a Claude Code Plugin Instead

Context7 also provides an official Claude Code plugin, which can be easier if you prefer managing integrations directly inside Claude Code.

Open Claude Code:

```
```
claude
```
```

Run the following commands one at a time:

```
```
/plugin marketplace add upstash/context7
```
```

```
```
/plugin install context7@context7-marketplace
```
```

Restart Claude Code and enter:

```
```
/mcp
```
```

Select Context7 and follow the browser authentication process.

The plugin connects to the hosted Context7 MCP server and exposes the same documentation lookup tools. Unlike the CLI setup, the plugin does not require you to install Node.js or run

```
npx
```

locally.

It also supports browser-based sign-in without manually configuring an API key. You only need one working Context7 integration. There is no benefit to registering duplicate MCP servers.

## Step 7: Configuring Context7 Manually With an API Key

For developers who prefer direct control, Context7 can also be installed manually.

First, visit the Context7 dashboard and create an API key.

Then run the following command in your terminal, replacing the placeholder with your key:

```
```
claude mcp add \
  --scope user \
  --transport http \
  context7 [https://mcp.context7.com/mcp](https://mcp.context7.com/mcp) \
  --header "Authorization: Bearer YOUR_API_KEY"
```
```

This connects Claude Code to the hosted Context7 server and makes the integration available across your projects.

Alternatively, you can run Context7 as a local MCP server using

```
npx
```

:

```
```
claude mcp add --scope user context7 -- \
  npx -y @upstash/context7-mcp \
  --api-key YOUR_API_KEY
```
```

For security, avoid putting actual API keys directly into shared configuration files, public repositories, or shell history. Prefer a secret manager or environment-variable-based configuration supported by your setup.

## Final Thoughts

Context7 does not replace testing, code reviews, or official documentation. However, it gives Claude Code a better starting point for generating code that matches the libraries you are actually using. I particularly like the ability to request documentation for specific library versions. It is useful when upgrading older projects or working with frameworks that frequently introduce breaking changes. You can learn more in the Context7 documentation.

Kanwal Mehreen is a machine learning engineer and a technical writer with a profound passion for data science and the intersection of AI with medicine. She co-authored the ebook "Maximizing Productivity with ChatGPT". As a Google Generation Scholar 2022 for APAC, she champions diversity and academic excellence. She's also recognized as a Teradata Diversity in Tech Scholar, Mitacs Globalink Research Scholar, and Harvard WeCode Scholar. Kanwal is an ardent advocate for change, having founded FEMCodes to empower women in STEM fields.
