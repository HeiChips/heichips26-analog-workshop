MAKEFILE_DIR := $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

PDK_ROOT ?= $(MAKEFILE_DIR)/IHP-Open-PDK
PDK ?= ihp-sg13cmos5l

PDK_REPO_IHP_OPEN_PDK ?= https://github.com/iic-jku/IHP-Open-PDK.git
PDK_COMMIT_IHP_OPEN_PDK ?= a70a2b692075535d7133994c514fd0e09f17a920

PDK_REPO_IHP_CMOS5L ?= https://github.com/iic-jku/ihp-sg13cmos5l.git
PDK_COMMIT_IHP_CMOS5L ?= c18379d6d1b54d70bc40231a456b4c6662631d72

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-20s %s\n", $$1, $$2}'
.PHONY: help

$(PDK_ROOT)/$(PDK):
	mkdir -p $(PDK_ROOT)
	git clone $(PDK_REPO_IHP_OPEN_PDK) --recurse-submodules --depth=1 --revision $(PDK_COMMIT_IHP_OPEN_PDK) $(PDK_ROOT)
	git clone $(PDK_REPO_IHP_CMOS5L) --recurse-submodules --depth=1 --revision $(PDK_COMMIT_IHP_CMOS5L) $(PDK_ROOT)/$(PDK)

clone-pdk: $(PDK_ROOT)/$(PDK) ## Clone the IHP-Open-PDK repository
.PHONY: clone-pdk
