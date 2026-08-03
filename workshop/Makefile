# SPDX-FileCopyrightText: 2026 The HeiChips Contributors
# SPDX-License-Identifier: Apache-2.0

all: fig-pdf
	quarto render index.qmd

# Local Windows helper: the standalone rsvg-convert build ignores -o when Quarto passes -a, so pre-convert the SVG figures.
# Quarto reuses an existing fig/*.pdf instead of converting. The PDFs are gitignored, so CI still converts them itself with its own librsvg.
fig-pdf:
	for f in fig/*.svg; do \
		out="$${f%.svg}.pdf"; \
		if [ ! -f "$$out" ] || [ "$$f" -nt "$$out" ]; then \
			rsvg-convert -f pdf -o "$$out" "$$f"; \
		fi \
	done
.PHONY: fig-pdf
