# JJK Hand Signs

Webcam-based hand gesture recognition that detects Jujutsu Kaisen hand signs and triggers real-time visual effects.

Work in progress.

## Gesture Guide

Each sign is built from simple single-hand shapes:

- **Point:** fist with only the index finger extended, thumb tucked
- **Open:** all five fingers extended and spread

| Sign | Pose |
|---|---|
| **Red** | One hand in the Point shape |
| **Blue** | Two Open hands, palms facing each other, held apart |
| **Purple** | One hand Point, the other hand Open, held apart (either hand can point) |
| **Domain Expansion** | Two hands with fingers interlaced |

Domain Expansion is the only sign that uses overlapping hands. Webcam hand tracking loses one hand when the hands overlap, so every other sign keeps both hands fully visible and apart.