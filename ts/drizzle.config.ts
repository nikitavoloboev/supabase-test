import { defineConfig } from "drizzle-kit"

export default defineConfig({
  schema: "./schema/schema.ts",
  out: "./db",
  dialect: "postgresql",
  dbCredentials: {
    url: process.env.DATABASE_URL!,
  },
  verbose: true,
  strict: true,
})
