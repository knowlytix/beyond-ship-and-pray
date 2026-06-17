"""Swappable LLM backend for the demo judge.

The judge is provider-agnostic: it needs any `forgeloop` ``BaseLM`` — i.e. any
object with ``.complete(prompt) -> str``. Configure it with environment
variables (no code change to switch vendors):

    LLM_PROVIDER = anthropic | openai | qwen | mock     (default: auto-detect)
    LLM_MODEL    = a model id for that provider          (sensible default each)

Keys are read from the provider's env var, or a dotfile fallback:
    anthropic -> ANTHROPIC_API_KEY  (or ~/.anthropic_key)
    openai    -> OPENAI_API_KEY     (or ~/.openai_key)

`qwen` runs a local model (no key); `mock` is the offline fallback. Bring your
own: anything with ``.complete(prompt)`` works in place of these.
"""

from __future__ import annotations

import _env  # noqa: F401  (auto-loads demos/.env)

import os

_DEFAULT_MODEL = {"anthropic": "claude-sonnet-4-6", "openai": "gpt-4o-mini"}


def _key(env_var: str, dotfile: str) -> str | None:
    k = os.environ.get(env_var)
    if not k:
        p = os.path.expanduser(dotfile)
        if os.path.exists(p):
            k = open(p).read().strip()
    return k or None


class OpenAIAdapter:
    """Minimal BaseLM over the OpenAI SDK — shows any .complete() backend plugs in."""

    def __init__(self, model: str = "gpt-4o-mini", api_key: str | None = None) -> None:
        from openai import OpenAI  # imported lazily so the SDK is only needed if used

        self._client = OpenAI(api_key=api_key or os.environ.get("OPENAI_API_KEY"))
        self._model = model

    def complete(self, prompt: str, **kwargs) -> str:
        resp = self._client.chat.completions.create(
            model=self._model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=kwargs.get("max_tokens", 256),
        )
        return resp.choices[0].message.content or ""


def _mock():
    from forgeloop.models import MockLM
    return MockLM(), "Mock (offline fallback)"


def build_judge_lm():
    """Return (lm, display_name) for the configured provider. Falls back to Mock."""
    provider = os.environ.get("LLM_PROVIDER", "auto").lower()
    model = os.environ.get("LLM_MODEL") or None

    def anthropic():
        k = _key("ANTHROPIC_API_KEY", "~/.anthropic_key")
        if k:
            from forgeloop.models import AnthropicAdapter
            m = model or _DEFAULT_MODEL["anthropic"]
            return AnthropicAdapter(model=m, api_key=k), f"Anthropic {m}"

    def openai():
        k = _key("OPENAI_API_KEY", "~/.openai_key")
        if k:
            m = model or _DEFAULT_MODEL["openai"]
            return OpenAIAdapter(model=m, api_key=k), f"OpenAI {m}"

    def qwen():
        from forgeloop.models import QwenAdapter
        return QwenAdapter(), f"Qwen local ({model or 'default'})"

    try:
        if provider == "anthropic":
            return anthropic() or _mock()
        if provider == "openai":
            return openai() or _mock()
        if provider == "qwen":
            return qwen()
        if provider == "mock":
            return _mock()
        # auto: first provider with credentials, else mock
        return anthropic() or openai() or _mock()
    except Exception as e:  # never let provider setup break the demo
        lm, _ = _mock()
        return lm, f"Mock (fallback: {type(e).__name__})"
