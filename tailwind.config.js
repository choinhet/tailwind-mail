/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./tailwind_mail/**/*.{html,js,css,py,jinja}"],
  theme: {
    extend: {},
  },
  plugins: [
    require("daisyui")
  ]
}

