# ChatBot Framework

A modular, extensible Python framework for building chatbot applications. Designed with clean architecture principles — composition over inheritance, separation of concerns, and plug-and-play extensions.

---

## Vision

Most chatbot implementations are monolithic scripts. This framework treats a chatbot as a composable object — a core engine that can be extended with optional modules like voice input, web scraping, RAG, and more — without touching the core.

---

## Architecture

### Core Classes

**`Client`**
Manages the connection to the LLM provider (OpenAI-compatible APIs).
Implemented as a **Singleton** — only one connection is ever created, no matter how many times it is instantiated.

**`Messages`**
Stores and manages the conversation history.
The LLM has no memory between API calls — this class is the memory. Every user message and assistant response is stored here and sent to the LLM on every turn.

**`ChatBotConfig`**
A configuration object that groups all chatbot parameters — client, model, messages, max tokens, and temperature. Keeps the `ChatBot` constructor clean.

**`ChatBot`**
The base chatbot class. Orchestrates the conversation loop through three overridable methods:
- `get_input()` — captures user input
- `ask_LLM()` — sends the conversation to the LLM and returns the response
- `deliver_output()` — presents the response to the user

---

### Extensions (Decorator Pattern)

Extensions wrap the base `ChatBot` without modifying it. They inherit from `ChatBot` and use aggregation to wrap any chatbot instance.

**`VoiceChatBot(ChatBot)`**
Overrides `get_input()` to capture audio from the microphone and convert it to text using Google Speech Recognition. The LLM interaction and output remain unchanged.

Usage:
```python
chatbot = ChatBot(config)
voice_chatbot = VoiceChatBot(chatbot)
voice_chatbot.talk()
```

---

### Scraper Module

The scraper is a **standalone utility**, not a chatbot extension. It fetches content from the web and returns clean text that can be injected into the `Messages` object as context for the LLM.

**`BaseScraper`**
Abstract base class with a single `scrape(url)` method.

**`BeautifulSoupScraper(BaseScraper)`**
Fetches and parses static HTML pages. Best for simple, fast scraping.

> **Planned:** `SeleniumScraper` for JavaScript-rendered pages, `ScrapyScraper` for structured XPath-based extraction.

Injecting scraped content:
```python
scraper = WebScraper()
content = scraper.scrape("https://example.com")
messages.add_message("system", f"Relevant context: {content}")
```

---

## Design Principles

- **Singleton** — one LLM connection, shared everywhere
- **Decorator Pattern** — extensions wrap the chatbot without modifying it
- **Separation of Concerns** — input, LLM call, and output are isolated methods
- **Composability** — mix and match extensions freely

---

## Planned Extensions

- `RAGChatBot` — Retrieval Augmented Generation
- `SeleniumScraper` — dynamic page scraping
- `DocumentChatBot` — chat over uploaded documents
- Wake word detection for smart mirror / voice assistant use cases

---

## Installation

```bash
pip install openai requests beautifulsoup4 speechrecognition pyaudio
```

---

## Quick Start

```python
from ClientClass import Client
from MessagesClass import Messages
from Response_typeClass import ChatBotConfig
from ChatClass import ChatBot

client = Client("OPENAI_API_KEY", "https://openrouter.ai/api/v1")
messages = Messages()
messages.add_message("system", "You are a helpful assistant.")
config = ChatBotConfig(client.get_client(), "openai/gpt-4", messages, 500, 0.7)
chatbot = ChatBot(config)
chatbot.talk()
```

---

## Use Case: Smart Mirror Assistant

This framework was initially built for a smart mirror assistant that:
1. Listens for a wake word
2. Activates the voice chatbot
3. Answers questions about IEEE INSAT using scraped web content

---

*Built by Dorra — INSAT, Tunis, 2026*