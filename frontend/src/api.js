const apiEndpoint = `http://localhost:5000`;

export function createApiCalls(modelName) {
  const endpoint = `${apiEndpoint}/${modelName}`;
  const internalModelName = modelName;
  return {
    get: async function() {
      const res = await fetch(endpoint);
      return await res.json();
    },
    post: async function(model) {
      const res = await fetch(endpoint, {
        method: 'POST',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'same-origin',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(model)
      });
      return await res.json();
    },
    update: async function(model) {}
  };
}
