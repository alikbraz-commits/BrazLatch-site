import { defineCollection, z } from "astro:content";

const pages = defineCollection({
  type: "content",
  schema: z.object({
    title: z.string(),
    description: z.string(),
    headline: z.string().optional(),
    subhead: z.string().optional(),
    ogImage: z.string().optional(),
  }),
});

const applications = defineCollection({
  type: "content",
  schema: z.object({
    title: z.string(),
    headline: z.string(),
    icon: z.string(),
    order: z.number(),
    description: z.string(),
  }),
});

export const collections = { pages, applications };
