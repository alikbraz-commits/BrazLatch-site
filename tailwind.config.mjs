/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,ts,tsx,vue,svelte}'],
  theme: {
    extend: {
      colors: {
        brand: {
          // --- Legacy names kept as aliases (values warmed) so existing components keep working ---
          black:        '#0E0D0B',  // was #0a0a0a — warm off-black, primary dark surface
          white:        '#EFEAE0',  // was #ffffff — bone, primary text on dark
          cream:        '#F4EEE2',  // was #f5f1ea — warmer paper
          ink:          '#1A1714',  // was #1a1a1a — warmer text-on-paper
          muted:        '#7A7468',  // was #6b7280 — warmer neutral muted

          // --- New semantic surfaces (Phase 2 components target these) ---
          'ink-deep':   '#16140F',  // section delineation on dark
          'ink-soft':   '#22201A',  // raised dark surface, scrollbar
          paper:        '#F4EEE2',  // alias of cream
          'paper-soft': '#EDE5D2',  // warm kraft, secondary light surface
          'paper-deep': '#1A1714',  // alias of ink (text on paper)

          // --- Type-tone aliases (semantic naming for new components) ---
          bone:         '#EFEAE0',  // alias of white (primary text on dark)
          'bone-muted': '#A8A296',  // secondary text on dark
          'bone-faint': '#5C574E',  // micro labels, dividers on dark
          'ink-muted':  '#5C574E',  // secondary text on paper
          'ink-faint':  '#8A8478',  // micro labels on paper

          // --- Accent system: three colors, three roles ---
          green:        '#009444',  // PRIMARY — official brand green (from logo PDF). CTAs, active state, "protected/licensed/proven"
          'green-deep': '#006D31',  // darker shade for hover states + engineering accent on light surfaces
          amber:        '#C46A2E',  // INDUSTRIAL — opportunity, open markets, manufacturing
          'amber-deep': '#7A4318',  // amber on light surfaces

          // --- Status semantics (aliases of accents) ---
          'status-licensed': '#009444',
          'status-open':     '#C46A2E',
          'status-caution':  '#D4A24C',
        },
      },
      fontFamily: {
        // Default sans — industrial, IBM-engineered humanist
        sans:    ['"IBM Plex Sans"', 'system-ui', '-apple-system', 'Segoe UI', 'sans-serif'],
        display: ['"IBM Plex Sans"', 'system-ui', 'sans-serif'],
        // Mono — JetBrains Mono used as a primary brand voice (patent #s, specs, labels)
        mono:    ['"JetBrains Mono"', 'ui-monospace', 'SFMono-Regular', 'monospace'],
        // Editorial serif — restricted to storytelling moments only (About, story pull-quotes)
        serif:   ['"Newsreader"', 'ui-serif', 'Georgia', 'serif'],
      },
      fontSize: {
        spec:         ['11px', { lineHeight: '1.3',  letterSpacing: '0.18em' }],
        'spec-lg':    ['13px', { lineHeight: '1.4',  letterSpacing: '0.14em' }],
        'display-xl': ['clamp(2.75rem, 5vw, 4.5rem)', { lineHeight: '1.02', letterSpacing: '-0.02em' }],
        'display-lg': ['clamp(2.25rem, 4vw, 3.5rem)', { lineHeight: '1.05', letterSpacing: '-0.018em' }],
        'display-md': ['clamp(1.75rem, 3vw, 2.5rem)', { lineHeight: '1.1',  letterSpacing: '-0.012em' }],
      },
      letterSpacing: {
        widest:       '0.18em',     // kept (existing usage in components)
        spec:         '0.18em',
        'spec-tight': '0.08em',
        display:      '-0.02em',
      },
      maxWidth: {
        prose:          '70ch',     // kept (existing usage)
        'prose-narrow': '52ch',     // new — editorial moments
        spec:           '88ch',     // new — spec strips
      },
      borderRadius: {
        spec: '2px',                // new — hard-edged technical card variant
      },
      boxShadow: {
        spec:         '0 1px 0 0 rgba(239, 234, 224, 0.04) inset',
        'card-warm':  '0 1px 24px -8px rgba(0,0,0,0.45), 0 0 0 1px rgba(239,234,224,0.04) inset',
        'card-green': '0 8px 32px -12px rgba(0,148,68,0.22), 0 0 0 1px rgba(0,148,68,0.20) inset',
        'card-amber': '0 8px 32px -12px rgba(196,106,46,0.18), 0 0 0 1px rgba(196,106,46,0.15) inset',
      },
      transitionTimingFunction: {
        mechanical: 'cubic-bezier(0.2, 0.7, 0.2, 1)',
        precise:    'cubic-bezier(0.4, 0, 0.2, 1)',
        settle:     'cubic-bezier(0.16, 0.84, 0.44, 1)',
      },
    },
  },
  plugins: [],
};
