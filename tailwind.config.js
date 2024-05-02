/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./docs/**/*.{md,html}"],
  theme: {
    extend: {
      colors: {
        primary: "#455FE9",
        primaryText: '#212529',
        secondaryText: '#495057',
      },
      fontFamily: {
        lato: ['lato'],
      },
    },
  },
  plugins: [],
};
