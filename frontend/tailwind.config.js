/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        coffee: {
          500: '#8c6b5d',
          900: '#3e2723',
        }
      }
    },
  },
  plugins: [],
}