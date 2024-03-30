/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./docs/**/*.{md,html}"],
  theme: {
    extend: {
      colors: {
        primary: "#455FE9",
      }
    },
    textColors: {
      'primary': '#212529',
      'secondary': '#495057',
    },
    fontFamily: {
      lato: ['lato'],
    },
  },
  plugins: [],
};
