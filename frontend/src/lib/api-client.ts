/**
 * Thin fetch wrapper for talking to the FastAPI backend.
 *
 * Every backend call should go through `apiFetch` so the base URL, JSON
 * headers, and error handling live in one place. TanStack Query hooks
 * (added per-feature in later milestones) call this instead of raw fetch.
 */

const API_BASE_URL = "http://localhost:8000/api/v1";

export class ApiError extends Error {
  constructor(
    message: string,
    public status: number,
  ) {
    super(message);
    this.name = "ApiError";
  }
}

export async function apiFetch<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    headers: { "Content-Type": "application/json", ...init?.headers },
    ...init,
  });

  if (!response.ok) {
    throw new ApiError(`Request to ${path} failed`, response.status);
  }

  return response.json() as Promise<T>;
}
