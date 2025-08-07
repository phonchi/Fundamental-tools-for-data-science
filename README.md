# 資料科學的基礎工具

歡迎來到資料科學的基礎工具！這份文件將引導你完成所有必要的環境安裝與帳號申請。讓我們開始吧！

---

## 1. 研究環境安裝 (Local Environment Setup)

有效率的本地環境是研究工作的基礎。我們將在 Windows 上透過 WSL 建立一個 Linux 環境。

* **建議**：若已經有Linux或Mac系統，又或者是windows系統但只想單純用 Mobaxterm 搭配 Git for windows練習則可以跳過WSL的安裝。
  
| 工具 | 這是什麼？ | 為什麼需要？ | 安裝指引 |
| :--- | :--- | :--- | :--- |
| **WSL** | Windows Subsystem for Linux | 在 Windows 上無縫運行一個完整的 Linux 環境。許多研究或論文用的工具和軟體原生於 Linux，因此通常對Linux支援較早且較完整。WSL 讓你能使用同樣強大的工具鏈，為未來的學術研究打好基礎。 | 打開你的 Windows 終端機 (PowerShell 或命令提示字元)，輸入 `wsl --install` 並按下 Enter。詳細指引請參考 [微軟官方文件](https://learn.microsoft.com/zh-tw/windows/wsl/install)。 |
| **MobaXterm** | 功能強大的 Windows 終端機軟體 | 它比 Windows 內建的終端機更好用，特別是在與 WSL 整合、需要遠端連線到實驗室伺服器、或需要圖形介面時，功能非常全面。 | 前往 [MobaXterm 官方網站](https://mobaxterm.mobatek.net/download.html) 下載並安裝 Home Edition (免費版)。 |
| **Git** | 程式碼與研究歷程的「時光機」 | 一個「版本控制」系統。它能追蹤你的程式碼、報告、論文的每一次修改，讓你安心進行各種實驗，不怕改壞成果，也可以當作與同學或指導教授協作的基礎。 | 前往 [Git 官方網站](https://git-scm.com/downloads) 下載並安裝。 (Mac 與 Linux 用戶通常已內建，可在終端機輸入 `git --version` 檢查)。 |

---

## 2. 帳號申請 (Essential Accounts)

資料科學研究是一個高度依賴社群與雲端資源的領域。以下平台將是你的知識庫、專題展示與雲端運算中心。

* **建議**：這門課會重點講授，若以後有要上相關課程建議申請。
  
| 平台 | 這是什麼？ | 為什麼需要？ | 申請指引 |
| :--- | :--- | :--- | :--- |
| **GitHub** | 全球最大的程式碼托管平台 | 備份你的 Git 專案、與他人進行學術協作、學習老手撰寫的程式碼。一個活躍的 GitHub 帳號也可以呈現學習軌跡與專案成果為履歷加分。 | 前往 [GitHub 官方網站](https://github.com/) 點擊 "Sign up" 進行註冊。 |
| **Google Colab** | Google 提供的免費雲端 Jupyter Notebook | 無需在本機安裝複雜環境，即可開始撰寫 Python、R與Julia 程式碼、訓練機器學習模型，甚至能免費使用強大的 GPU 資源，是進行深度學習研究的利器。 | 使用你的 Google 帳號，前往 [Colab 官方網站](https://colab.research.google.com/) 即可開始使用。 |
| **Kaggle** | 全球最大的資料科學學習平台，也有提供的免費雲端 Jupyter Notebook和背景執行功能 | 可以在這裡找到海量的數據集來做專題報告或論文研究、參加競賽磨練實力、並觀摩全世界研究者是如何分析問題與撰寫程式碼的 (Notebooks)。 | 前往 [Kaggle 官方網站](https://www.kaggle.com/) 點擊 "Register" 進行註冊。 |

---

## 3. AI 學習助理 (AI Learning Assistants)

AI 助理就像一位 24 小時待命的資深學長姐或老師，能幫你寫程式、除錯、解釋艱澀概念、學習新知，大幅提升你的學習與研究效率。

* **建議**：至少熟悉其中一到兩款，它們在不同任務上各有千秋。
* **注意**：**切勿**將任何個人隱私、或未公開的學術研究數據輸入給任何 AI 助理。

| AI 助理 | 簡介 | 註冊連結 |
| :--- | :--- | :--- |
| **Google Gemini** | Google 推出的多模態 AI 模型，整合在 Google 生態系中，對程式碼的理解與生成能力很強。 | [前往 Gemini](https://gemini.google.com/) |
| **OpenAI ChatGPT** | 最廣為人知的對話式 AI，生態系龐大，可用功能最多，擁有豐富的插件與應用。 | [前往 ChatGPT](https://chat.openai.com/) |
| **GitHub Copilot** | 由 GitHub 與 OpenAI 合作開發，深度整合在 VS Code 等編輯器中，提供極為流暢的程式碼自動補全體驗。亦可直接在GitHub網站做使用。 | [前往 Copilot](https://github.com/features/copilot) (學生通常可透過 GitHub Student Developer Pack 申請免費使用) |
| **Anthropic Claude** | 由前 OpenAI 員工創立的公司開發，以其超長的上下文處理能力和更謹慎安全的對話風格著稱。在程式方面的能力也很強。 | [前往 Claude](https://claude.ai/) |

---

## 4. 命令列介面 (CLI) 工具安裝

CLI (Command-Line Interface) 讓你可以在終端機裡，直接與上述雲端AI互動，實現更高效的自動化研究流程。

* **建議**：熟悉其中一款，讓管理專案更輕鬆。
* **注意**：**切勿**將任何個人隱私、或未公開的學術研究數據輸入給任何 AI 助理。
    
| CLI 工具 | 這是什麼？ | 為什麼需要？ | 安裝指引 |
| :--- | :--- | :--- | :--- |
| **Gemini CLI (`gemini`)** | Google Gemini 的官方命令列工具 | 在終端機裡與 Gemini 互動，可以讀取本地檔案 (`@file`)、執行系統指令 (`!cmd`)，實現強大的研究流程自動化。 | 建議使用nodejs流程安裝，參考[這裡](https://vocus.cc/article/6863fcb9fd897800014e018d) |
| **Codex CLI** | Open AI 的官方命令列工具 | ChatGPT 也提供了 CLI 工具或 API，讓你能將它們的能力整合到終端機中，輔助你的研究。 | 參考 [這裡](https://www.communeify.com/tw/blog/openai-codex-cli-ai-code-terminal/) 安裝。 |
| **GitHub CLI (`gh`)** | GitHub 的官方命令列工具 | 在終端機裡直接管理你的 Repository、與同學協作，無需頻繁切換到瀏覽器，讓你的研究工作流一氣呵成。 | 參考 [GitHub CLI 官方安裝文件](https://docs.github.com/en/copilot/how-tos/use-copilot-for-common-tasks/use-copilot-in-the-cli)。 |
| **Claude code** | Anthropic 的官方命令列工具 | Claude 也提供了 CLI 工具或 API，讓你能將它們的能力整合到終端機中，輔助你的研究。 | 參考 [Anthropic API 文件](https://docs.anthropic.com/zh-TW/docs/claude-code/setup)安裝。 |

---

## 5. 開發與編輯環境 (IDE & Notebooks) (選用)

雖然Colab已經是強大的IDE，但他著重在探索式分析和實驗。如果能選擇合適的開發環境能進一步提升研究和寫程式效率。以下是幾種主流的選擇，你可以根據你的主要使用語言和專案需求來決定。

* **建議**：選用不一定需要，**這門課也不會探討**。
  
| 工具 | 這是什麼？ | 為什麼需要？ | 安裝指引 & AI 整合 |
| :--- | :--- | :--- | :--- |
| **Visual Studio Code (選用)** | 微軟開發的免費、強大的程式碼編輯器。 | 擁有極為豐富的擴充套件生態系，可以完美整合 Python、Git、Jupyter Notebook 等。讓你能在同一個視窗中完成寫程式、版本控制、做筆記等所有事情，是學術界最受歡迎的編輯器之一。 | 前往 [VS Code 官方網站](https://code.visualstudio.com/) 下載。可透過擴充套件安裝 **GitHub Copilot** 等 AI 助理。 |
| **Cursor (選用)** | 一個內建 AI 功能的 VS Code 分支。 | 它本質上就是 VS Code，但深度整合了 AI 對話、程式碼生成與編輯功能。你可以直接在編輯器中與你的整個專案程式碼庫對話，非常適合用來理解複雜的專案或進行大型重構。 | 前往 [Cursor 官方網站](https://cursor.sh/) 下載並安裝。 |
| **RStudio (R語言使用者)** | 專為 R 語言打造的整合開發環境 (IDE)。 | 如果你的研究或課程大量使用 R 語言進行統計分析與視覺化，RStudio 提供了無可比擬的整合體驗，包含程式碼、圖表、終端機和變數檢視器。 | 前往 [Posit 官方網站](https://posit.co/download/rstudio-desktop/) 下載。可透過擴充套件整合 [**GitHub Copilot**](https://docs.posit.co/ide/user/ide/guide/tools/copilot.html)。 (需先安裝 R 語言本身)。 |
| **MATLAB (工程領域使用者)** | 一個高效能的數值計算與視覺化軟體。 | 在工程、信號處理、控制系統等領域是標準工具。其豐富的工具箱 (Toolbox) 和直觀的矩陣運算，讓複雜的數學建模與模擬變得相對簡單。 | 屬商業軟體，但多數大學提供校園授權。[新版 **MATLAB 已內建 AI 功能**](https://www.mathworks.com/products/matlab-copilot.html)，如程式碼建議等。中山大學提供主程式與AI授權請參考[這裡](https://lis.nsysu.edu.tw/p/405-1001-194308,c11666.php?Lang=zh-tw)。 |
| **Jupyter Notebook (本地端)** | 在你自己的電腦上運行的互動式筆記本環境。 | 讓你能在沒有網路連線的情況下進行資料分析，並完全掌控你的運算環境與套件版本。適合處理敏感資料或需要高度客製化環境的研究。 | 最簡單的方式是透過安裝 [Anaconda 發行版](https://www.anaconda.com/download)。可透過安裝 [**Jupyter AI**](https://github.com/jupyterlab/jupyter-ai) 擴充套件來整合各種大型語言模型 (建議可以搭配 [Ollama](https://ollama.com/))。 |

---

## 6. 參考資源

* **LLM 相關指令教學**：可參考此 HackMD 文件來學習更多與大型語言模型互動的技巧：[https://hackmd.io/@phonchi/LLM_Basic](https://hackmd.io/@phonchi/LLM_Basic)

## 7. LLM功能比較矩陣


### 1. 核心模型與推理
| 功能 | OpenAI ChatGPT | Google Gemini | Anthropic Claude | Microsoft Copilot |
| :-- | :-- | :-- | :-- | :-- |
| **基礎模型引擎** | GPT-4o、`o` 系列 (o3, o4-mini) [[原文]](https://openai.com/index/hello-gpt-4o/) | Gemini 2.5 系列 (Pro, Flash) [[原文]](https://blog.google/products/gemini/google-gemini-2-5-pro-flash/) | Claude 4.1、3.5 Sonnet [[原文]](https://www.anthropic.com/news/claude-3-5-sonnet) | 基於 GPT-4o [[原文]](https://blogs.microsoft.com/blog/2024/05/20/microsoft-build-2024-news/) |
| **最大上下文視窗** | 128 k (GPT-4o) [[原文]](https://openai.com/api/pricing/) | 100 萬 (可擴 200 萬)  | 20 萬  | 128 k [[原文]](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/) |
| **高階推理模式** | `o` 系列複雜任務模式  | **Deep Think** [[原文]](https://blog.google/products/gemini/gemini-drop-july-2025/) | **擴展思維** [[原文]](https://www.anthropic.com/news/expanded-thought-process-for-claude) | — |
| **API 成本 / 層級** | o3、o4-mini 等多層級 [[原文]](https://openai.com/api/pricing/) | Pro、Flash、Flash-Lite 等 [[原文]](https://ai.google.dev/pricing) | Opus、Sonnet、Haiku 等 [[原文]](https://www.anthropic.com/pricing) | 透過 Azure OpenAI [[原文]](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/) |


### 2. 互動式工作空間
| 功能 | OpenAI ChatGPT | Google Gemini | Anthropic Claude | Microsoft Copilot |
| :-- | :-- | :-- | :-- | :-- |
| **官方名稱** | **Canvas**（創作）<br/>**Projects**（組織） [[原文]](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt) | **Canvas** [[原文]](https://support.google.com/gemini/answer/15074900) | **Artifacts** [[原文]](https://www.anthropic.com/news/claude-3-5-sonnet) | **Pages** [[原文]](https://support.microsoft.com/en-us/office/get-started-with-copilot-pages-in-microsoft-copilot-for-microsoft-365-298f244a-9b59-4c8d-93d3-78b0f79b0687) |
| **核心哲學** | 即時共同創作 + 長期上下文 | 快速原型與創意沙盒 | 即時 IDE 體驗 | 企業協作文件 |
| **即時程式碼執行** | 支援 Python、HTML/React [[原文]](https://help.openai.com/en/articles/9930697-what-is-the-canvas-feature-in-chatgpt-and-how-do-i-use-it) | 支援（生成型 App） | 支援 HTML/React | 不支援 |
| **協作編輯** | 用戶×AI 同步共編 | 支援多用戶資料共享 | 不支援多人同編 | 完整多人共編 [[原文]](https://techcommunity.microsoft.com/t5/microsoft-365-copilot/copilot-pages-now-available-in-microsoft-copilot-for-microsoft/m-p/4126130) |
| **分享 / 部署** | Canvas 可分享；Projects 私有 | 分享生成 App | 分享互動式 Artifact | 透過 Teams / Outlook 分享 [[原文]](https://support.microsoft.com/en-us/office/share-a-loop-component-7954dd12-8419-47f2-8958-c39e24564c48) |


### 3. 檔案與數據處理
| 功能 | OpenAI ChatGPT | Google Gemini | Anthropic Claude | Microsoft Copilot |
| :-- | :-- | :-- | :-- | :-- |
| **檔案上傳來源** | 本機、Google Drive、OneDrive [[原文]](https://help.openai.com/en/articles/10169530-connecting-google-drive-and-onedrive-to-chatgpt) | 本機、Google Drive、GitHub [[原文]](https://support.google.com/gemini/answer/14903178) | 本機（Files API） | 本機、OneDrive、SharePoint [[原文]](https://learn.microsoft.com/en-us/microsoft-365-copilot/microsoft-365-copilot-overview) |
| **最大檔案大小** | 512 MB [[原文]](https://help.openai.com/en/articles/9233636-what-are-the-file-size-limits-for-file-uploads-in-chatgpt) | 100 MB；影片 2 GB [[原文]](https://support.google.com/gemini/answer/14903178) | 500 MB [[原文]](https://docs.anthropic.com/en/docs/build-with-claude/files) | 512 MB [[原文]](https://learn.microsoft.com/en-us/microsoft-365-copilot/microsoft-365-copilot-faq#what-are-the-limitations-of-copilot-) |
| **持久性儲存** | **Projects** | 無 | **Files API** | 依賴 OneDrive / SharePoint |
| **資料分析環境** | 內建 Python 沙盒 [[原文]](https://openai.com/blog/data-analysis-improvements) | Python 沙盒 + BigQuery / Sheets | Python 沙盒 & Claude Code [[原文]](https://docs.anthropic.com/en/docs/build-with-claude/code-interpreter) | Excel 中的 Python & Microsoft Fabric [[原文]](https://techcommunity.microsoft.com/t5/excel-blog/announcing-python-in-excel-combining-the-power-of-python-and-the/ba-p/3905488) |


### 4. 代理式能力
| 功能 | OpenAI ChatGPT | Google Gemini | Anthropic Claude | Microsoft Copilot |
| :-- | :-- | :-- | :-- | :-- |
| **自主研究功能** | **Deep Research** [[原文]](https://openai.com/blog/deep-research) | **Deep Research** [[原文]](https://blog.google/products/gemini/gemini-drop-july-2025/) | 非品牌化通用能力 | **Deep Research** [[原文]](https://www.microsoft.com/en-us/microsoft-copilot/blog/2025/06/25/release-notes-june-25-2025/) |
| **自訂代理** | **Custom GPTs** [[原文]](https://openai.com/blog/introducing-gpts) | **Gems** [[原文]](https://blog.google/products/gemini/google-gemini-update-may-2024-gems/), [Jules](https://jules.google/) | API & Claude Code [[原文]](https://milvus.io/blog/claude-code-vs-gemini-cli-which-ones-the-real-dev-co-pilot.md) | **Copilot Studio** [[原文]](https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio) |
| **排程 / 主動動作** | 否（可透過 Actions） | **Scheduled Actions** [[原文]](https://blog.google/products/gemini/gemini-drop-july-2025/) | 否 | 否（可 Power Automate） |


### 5. 多模態能力
| 功能 | OpenAI ChatGPT | Google Gemini | Anthropic Claude | Microsoft Copilot |
| :-- | :-- | :-- | :-- | :-- |
| **圖像生成** | GPT-4o / DALL-E 3 | **Imagen 4** [[原文]](https://blog.google/products/gemini/google-imagen-4-generative-ai/) | —（策略性省略） [[原文]](https://www.anthropic.com/safety) | **DALL-E 3** [[原文]](https://create.microsoft.com/en-us/features/ai-image-generator) |
| **影片生成** | **Sora** | **Veo** [[原文]](https://blog.google/technology/ai/google-veo-io-2024/) | — | — |
| **音訊生成** | —（語音模式） | 生成式音訊 [[原文]](https://blog.google/technology/ai/google-gemini-generative-audio/) | —（語音模式） | — |
| **即時視覺輸入** | 行動裝置支援 | **Gemini Live** [[原文]](https://blog.google/products/gemini/google-gemini-live-io-2024/) | — | **Copilot Vision** [[原文]](https://www.microsoft.com/en-us/microsoft-copilot/blog/2025/06/25/release-notes-june-25-2025/) |


