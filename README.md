# 學術研究的基礎工具與環境設定

歡迎來到資料科學的研究領域！這份文件將引導你完成所有必要的環境安裝與帳號申請。打造一個穩定、高效的研究環境，是讓研究之路更順遂的第一步。讓我們開始吧！

---

## 1. 研究環境安裝 (Local Environment Setup)

有效率本地環境是所有研究工作的基礎。我們將在 Windows 上透過 WSL 建立一個 Linux 環境。

* **建議**：若已經有Linux或Mac又或者只想單純用Mobaxterm練習則可以跳過WSL的安裝。
  
| 工具 | 這是什麼？ | 為什麼需要？ | 安裝指引 |
| :--- | :--- | :--- | :--- |
| **WSL** | Windows Subsystem for Linux | 在 Windows 上無縫運行一個完整的 Linux 環境。許多研究用的工具和伺服器軟體原生於 Linux，WSL 讓你能使用同樣強大的工具鏈，為未來的學術研究打好基礎。 | 打開你的 Windows 終端機 (PowerShell 或命令提示字元)，輸入 `wsl --install` 並按下 Enter。詳細指引請參考 [微軟官方文件](https://learn.microsoft.com/zh-tw/windows/wsl/install)。 |
| **MobaXterm** | 功能強大的 Windows 終端機軟體 | 它比 Windows 內建的終端機更好用，特別是在與 WSL 整合、需要遠端連線到實驗室伺服器、或需要圖形介面時，功能非常全面。 | 前往 [MobaXterm 官方網站](https://mobaxterm.mobatek.net/download.html) 下載並安裝 Home Edition (免費版)。 |
| **Git** | 程式碼與研究歷程的「時光機」 | 一個「版本控制」系統。它能追蹤你的程式碼、報告、論文的每一次修改，讓你安心進行各種實驗，不怕改壞成果，是與同學或指導教授協作的基礎。 | 前往 [Git 官方網站](https://git-scm.com/downloads) 下載並安裝。 (Mac 與 Linux 用戶通常已內建，可在終端機輸入 `git --version` 檢查)。 |

---

## 2. 帳號申請 (Essential Accounts)

資料科學研究是一個高度依賴社群與雲端資源的領域。以下平台將是你的知識庫、專題展示間與雲端運算中心。

* **建議**：這門課會重點講授，若以後有要上相關課程建議申請。
  
| 平台 | 這是什麼？ | 為什麼需要？ | 申請指引 |
| :--- | :--- | :--- | :--- |
| **GitHub** | 全球最大的程式碼托管平台 | 備份你的 Git 專案、與他人進行學術協作、學習頂尖的程式碼。一個活躍的 GitHub 帳號可以呈現學習軌跡與專案成果。 | 前往 [GitHub 官方網站](https://github.com/) 點擊 "Sign up" 進行註冊。 |
| **Google Colab** | Google 提供的免費雲端 Jupyter Notebook | 無需在本機安裝複雜環境，即可開始撰寫 Python 程式碼、訓練機器學習模型，甚至能免費使用強大的 GPU 資源，是進行深度學習研究的利器。 | 使用你的 Google 帳號，前往 [Colab 官方網站](https://colab.research.google.com/) 即可開始使用。 |
| **Kaggle** | 全球最大的資料科學學習平台 | 可以在這裡找到海量的數據集來做專題報告或論文研究、參加競賽磨練實力、並觀摩全世界高手是如何分析問題與撰寫程式碼的 (Notebooks)。 | 前往 [Kaggle 官方網站](https://www.kaggle.com/) 點擊 "Register" 進行註冊。 |

---

## 4. AI 學習助理 (AI Learning Assistants)

AI 助理就像一位 24 小時待命的資深學長姐或老師，能幫你寫程式、除錯、解釋艱澀概念、學習新知，大幅提升你的學習與研究效率。

* **建議**：至少熟悉其中一到兩款，它們在不同任務上各有千秋。
* **注意**：**切勿**將任何個人隱私、或未公開的學術研究數據輸入給任何 AI 助理。

| AI 助理 | 簡介 | 註冊連結 |
| :--- | :--- | :--- |
| **Google Gemini** | Google 推出的多模態 AI 模型，整合在 Google 生態系中，對程式碼的理解與生成能力很強。 | [前往 Gemini](https://gemini.google.com/) |
| **OpenAI ChatGPT** | 最廣為人知的對話式 AI，生態系龐大，擁有豐富的插件與應用。 | [前往 ChatGPT](https://chat.openai.com/) |
| **GitHub Copilot** | 由 GitHub 與 OpenAI 合作開發，深度整合在 VS Code 等編輯器中，提供極為流暢的程式碼自動補全體驗。 | [前往 Copilot](https://github.com/features/copilot) (學生通常可透過 GitHub Student Developer Pack 申請免費使用) |
| **Anthropic Claude** | 由前 OpenAI 員工創立的公司開發，以其超長的上下文處理能力和更謹慎安全的對話風格著稱。 | [前往 Claude](https://claude.ai/) |

---

## 5. 命令列介面 (CLI) 工具安裝

CLI (Command-Line Interface) 讓你可以在終端機裡，直接與雲端服務互動，實現更高效的自動化研究流程。

* **建議**：熟悉其中一款，讓管理專案更輕鬆。
  
| CLI 工具 | 這是什麼？ | 為什麼需要？ | 安裝指引 |
| :--- | :--- | :--- | :--- |
| **Gemini CLI (`gemini`)** | Google Gemini 的官方命令列工具 | 在終端機裡與 Gemini 互動，可以讀取本地檔案 (`@file`)、執行系統指令 (`!cmd`)，實現強大的研究流程自動化。 | 建議使用nodejs流程安裝，參考[這裡](https://vocus.cc/article/6863fcb9fd897800014e018d) |
| **Codex CLI** | | ChatGPT 也提供了 CLI 工具或 API，讓你能將它們的能力整合到終端機中，輔助你的研究。 | 參考 [這裡](https://www.communeify.com/tw/blog/openai-codex-cli-ai-code-terminal/) 安裝。 |
| **GitHub CLI (`gh`)** | GitHub 的官方命令列工具 | 在終端機裡直接管理你的 Repository、與同學協作，無需頻繁切換到瀏覽器，讓你的研究工作流一氣呵成。 | 參考 [GitHub CLI 官方安裝文件](https://docs.github.com/en/copilot/how-tos/use-copilot-for-common-tasks/use-copilot-in-the-cli)。 |
| **Claude code** | | Claude 也提供了 CLI 工具或 API，讓你能將它們的能力整合到終端機中，輔助你的研究。 | 參考 [Anthropic API 文件](https://docs.anthropic.com/zh-TW/docs/claude-code/setup)安裝。 |

---

## 5. 開發與編輯環境 (IDE & Notebooks) (選用)

雖然Colab已經是強大的IDE，但他著重在探索式分析和實驗。如果能選擇合適的開發環境能進一步提升你的研究效率。以下是幾種主流的選擇，你可以根據你的主要使用語言和專案需求來決定。

* **建議**：選用不一定需要，**這門課也不會探討**。
  
| 工具 | 這是什麼？ | 為什麼需要？ | 安裝指引 & AI 整合 |
| :--- | :--- | :--- | :--- |
| **Visual Studio Code (選用)** | 微軟開發的免費、強大的程式碼編輯器。 | 擁有極為豐富的擴充套件生態系，可以完美整合 Python、Git、Jupyter Notebook 等。讓你能在同一個視窗中完成寫程式、版本控制、做筆記等所有事情，是學術界最受歡迎的編輯器之一。 | 前往 [VS Code 官方網站](https://code.visualstudio.com/) 下載。可透過擴充套件安裝 **GitHub Copilot** 等 AI 助理。 |
| **Cursor (選用)** | 一個內建 AI 功能的 VS Code 分支。 | 它本質上就是 VS Code，但深度整合了 AI 對話、程式碼生成與編輯功能。你可以直接在編輯器中與你的整個專案程式碼庫對話，非常適合用來理解複雜的專案或進行大型重構。 | 前往 [Cursor 官方網站](https://cursor.sh/) 下載並安裝。 |
| **RStudio (R語言使用者)** | 專為 R 語言打造的整合開發環境 (IDE)。 | 如果你的研究或課程大量使用 R 語言進行統計分析與視覺化，RStudio 提供了無可比擬的整合體驗，包含程式碼、圖表、終端機和變數檢視器。 | 前往 [Posit 官方網站](https://posit.co/download/rstudio-desktop/) 下載。可透過擴充套件整合 **GitHub Copilot**。 (需先安裝 R 語言本身)。 |
| **MATLAB (工程領域使用者)** | 一個高效能的數值計算與視覺化軟體。 | 在工程、信號處理、控制系統等領域是標準工具。其豐富的工具箱 (Toolbox) 和直觀的矩陣運算，讓複雜的數學建模與模擬變得相對簡單。 | 屬商業軟體，但多數大學提供校園授權，請洽詢學校 IT 部門。新版 **MATLAB 已內建 AI 功能**，如程式碼建議等。 |
| **Jupyter Notebook (本地端)** | 在你自己的電腦上運行的互動式筆記本環境。 | 讓你能在沒有網路連線的情況下進行資料分析，並完全掌控你的運算環境與套件版本。適合處理敏感資料或需要高度客製化環境的研究。 | 最簡單的方式是透過安裝 [Anaconda 發行版](https://www.anaconda.com/download)。可透過安裝 **Jupyter AI** 擴充套件來整合各種大型語言模型。 |

---

## 6. 參考資源

* **LLM 相關指令教學**：可參考此 HackMD 文件來學習更多與大型語言模型互動的技巧：[https://hackmd.io/@phonchi/LLM_Basic](https://hackmd.io/@phonchi/LLM_Basic)
