# Historical Notes: Why CUDA died on macOS

macOS support for NVIDIA GPUs ended due to strategic and technical shifts. This brief timeline records key events to preserve context for researchers.

## Timeline

- 2018: Last macOS releases with NVIDIA WebDriver support (High Sierra).
- 2018–2019: Apple stops signing new WebDrivers for Mojave and later.
- CUDA on macOS effectively frozen at 10.2.
- PyTorch and other DL frameworks drop official macOS CUDA support.

## NVIDIA / Apple Split

- Driver signing and kext policies limited third-party GPU enablement.
- Diverging priorities: Apple Metal vs third-party CUDA.

## Impact

- Loss of a once-viable DL platform on Apple hardware.
- Necessitates preservation work for historical reproducibility.

## Why Preserve

- Scientific reproducibility on legacy hardware
- Educational value: systems engineering, driver models, kernel policies
- Museum mode: document deprecation timelines and community responses