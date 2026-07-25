import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

/**
 * Merges Tailwind classes, resolving conflicts (e.g. "p-2 p-4" -> "p-4").
 * Standard shadcn/ui helper - components generated via `shadcn add` expect
 * this to exist at this exact path.
 */
export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
