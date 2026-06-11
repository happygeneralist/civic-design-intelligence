const statDefinitions = [
  ['markdown_objects', 'Markdown objects', 'Files counted in numbered knowledge-object folders.'],
  ['service_areas', 'Service areas', 'From service area or domain metadata.'],
  ['repository_areas', 'Repository areas', 'Numbered knowledge-object areas.'],
  ['user_needs', 'User needs', 'Classified by folder, metadata or ID.'],
  ['civic_needs', 'Civic needs', 'Classified by metadata or CN IDs.'],
  ['evidence', 'Evidence items', 'Evidence objects and files.'],
  ['pain_points', 'Pain points', 'Pain-point objects and files.'],
  ['insights', 'Insights', 'Insight objects and files.']
];

function formatValue(value) {
  return Number.isFinite(value) ? value.toLocaleString('en-GB') : '0';
}

function renderStats(stats) {
  const totals = stats.totals || {};
  const grid = document.getElementById('stats-grid');
  grid.innerHTML = statDefinitions.map(([key, label, hint]) => `
    <div class="stat">
      <span class="stat__value">${formatValue(totals[key])}</span>
      <span class="stat__label">${label}</span>
      <span class="stat__hint">${hint}</span>
    </div>
  `).join('');

  const generatedAt = stats.generated_at ? new Date(stats.generated_at).toLocaleString('en-GB') : 'unknown';
  document.getElementById('stats-metadata').innerHTML = `
    <strong>Last generated:</strong> ${generatedAt}<br>
    <strong>Source:</strong> ${stats.generated_from || 'Repository markdown files'}<br>
    ${stats.scope_note || ''}
  `;

  renderBreakdowns(stats);
}

function renderTable(title, data) {
  const entries = Object.entries(data || {}).sort((a, b) => b[1] - a[1]);
  if (!entries.length) return '';
  return `
    <section class="breakdown">
      <h3>${title}</h3>
      <table>
        <thead><tr><th>Category</th><th>Count</th></tr></thead>
        <tbody>
          ${entries.map(([key, value]) => `<tr><td>${key}</td><td>${formatValue(value)}</td></tr>`).join('')}
        </tbody>
      </table>
    </section>
  `;
}

function renderBreakdowns(stats) {
  document.getElementById('breakdowns').innerHTML = [
    renderTable('By status', stats.by_status),
    renderTable('By lifecycle state', stats.by_lifecycle_state),
    renderTable('By evidence strength', stats.by_evidence_strength)
  ].join('');
}

fetch('stats.json', { cache: 'no-store' })
  .then((response) => {
    if (!response.ok) throw new Error('Stats file not available yet');
    return response.json();
  })
  .then(renderStats)
  .catch((error) => {
    document.getElementById('stats-grid').innerHTML = `
      <div class="stat">
        <span class="stat__value">-</span>
        <span class="stat__label">Stats not generated yet</span>
        <span class="stat__hint">Run the Build GitHub Pages stats workflow.</span>
      </div>
    `;
    document.getElementById('stats-metadata').textContent = error.message;
  });
