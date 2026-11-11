import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { readdirSync } from 'fs'
import { resolve } from 'path'
import { fileURLToPath } from 'url'

const __dirname = fileURLToPath(new URL('.', import.meta.url))

const pages = Object.fromEntries(
  readdirSync(__dirname)
    .filter(f => f.endsWith('.html'))
    .map(f => [f.replace('.html', ''), resolve(__dirname, f)])
)

export default defineConfig({
  plugins: [react()],
  build: { rollupOptions: { input: pages } },
})