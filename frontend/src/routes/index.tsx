import { createBrowserRouter } from "react-router-dom";

/**
 * Route table for the app. Each page below is a placeholder - real page
 * components are built out in the "Web Application Pages" milestone. Kept
 * as a separate module (not inline in App.tsx) so adding a page is a
 * one-line change here rather than editing the provider tree.
 */

function Placeholder({ label }: { label: string }) {
  return (
    <div className="flex h-full items-center justify-center text-muted-foreground">
      {label} — coming in a future milestone
    </div>
  );
}

export const router = createBrowserRouter([
  { path: "/", element: <Placeholder label="Dashboard" /> },
  { path: "/reports", element: <Placeholder label="Reports" /> },
  { path: "/reports/:date", element: <Placeholder label="Daily Report" /> },
  { path: "/calendar", element: <Placeholder label="Calendar" /> },
  { path: "/analytics", element: <Placeholder label="Analytics" /> },
  { path: "/summary/weekly", element: <Placeholder label="Weekly Summary" /> },
  { path: "/summary/monthly", element: <Placeholder label="Monthly Summary" /> },
  { path: "/search", element: <Placeholder label="Search" /> },
  { path: "/settings", element: <Placeholder label="Settings" /> },
  { path: "/about", element: <Placeholder label="About" /> },
]);
