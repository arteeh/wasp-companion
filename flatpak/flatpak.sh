#!/bin/bash

rm -rf .builddir .flatpak-builder

# Remove current flatpak if it exists
flatpak remove --delete-data -y com.arteeh.Companion

# For refreshing the python module requirements
python3 ./flatpak-pip-generator --requirements-file=python.txt --output python

# Install
flatpak run org.flatpak.Builder .builddir com.arteeh.Companion.yml --force-clean --user --install

# Run
flatpak run com.arteeh.Companion
