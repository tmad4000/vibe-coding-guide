export function escapeHtml(input) {
  return String(input)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

export function markdownToHtml(markdown) {
  const escaped = escapeHtml(markdown || "");
  return escaped
    .replace(/^###\s(.+)$/gm, "<h3>$1</h3>")
    .replace(/^##\s(.+)$/gm, "<h2>$1</h2>")
    .replace(/^#\s(.+)$/gm, "<h1>$1</h1>")
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/\*(.+?)\*/g, "<em>$1</em>")
    .replace(/`(.+?)`/g, "<code>$1</code>")
    .replace(/\n/g, "<br>");
}

export function normalizeSurface(surface) {
  if (!surface || typeof surface !== "object") {
    return {
      type: "none",
      title: "",
      content: ""
    };
  }

  return {
    type: surface.type || "none",
    title: surface.title || "",
    content: surface.content || "",
    columns: Array.isArray(surface.columns) ? surface.columns : [],
    rows: Array.isArray(surface.rows) ? surface.rows : []
  };
}
