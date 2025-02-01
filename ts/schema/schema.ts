import { pgTable, text, timestamp, boolean, integer } from "drizzle-orm/pg-core"

export const user = pgTable("user", {
  id: text("id").primaryKey(),
  name: text("name").notNull(),
  email: text("email").notNull().unique(),
  emailVerified: boolean("email_verified").notNull().default(false),
  tokens: integer("tokens").notNull().default(0),
  createdAt: timestamp("created_at").notNull().defaultNow(),
  updatedAt: timestamp("updated_at").notNull().defaultNow(),
})

export const generation = pgTable("generation", {
  id: text("id").primaryKey(),
  createdByUser: text("user_id")
    .notNull()
    .references(() => user.id),
  prompt: text("prompt").notNull(),
  status: text("status").notNull(), // pending, completed, failed
  imageUrl: text("image_url"), // url of generated image
  createdAt: timestamp("created_at").notNull().defaultNow(),
})
