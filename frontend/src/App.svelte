<script>
  import { onMount } from 'svelte';
  import { createApiCalls } from './api';
  const userApi = createApiCalls('user');

  let users;
  let filteredUsers;
  let searchText = '';
  let selectedUser = null;

  let inputFirstName = '';
  let isInputFirstNameValid = false;
  let inputLastName = '';
  let isInputLastNameValid = false;
  let inputUserName = '';
  let isInputUserNameValid = false;
  let inputStreet = '';
  let isInputStreetValid = false;
  let inputCity = '';
  let isInputCityValid = false;
  let inputZip = '';
  let isInputZipValid = false;

  onMount(fetchUsers);

  async function fetchUsers() {
    try {
      const response = await userApi.get();
      users = response.data;
    } catch (err) {
      console.log('Something went wrong fetching users:', err);
    }
  }

  async function postUser() {
    const user = {
      first_name: inputFirstName,
      last_name: inputLastName,
      user_name: inputUserName,
      street: inputStreet,
      city: inputCity,
      zip: inputZip
    };
    try {
      const newUser = await userApi.post(user);
      users = [...users, newUser.data];
      clearFormInput();
    } catch (err) {
      console.log('Something went wrong posting the user:', err);
    }
  }

  function clearFormInput() {
    inputFirstName = '';
    inputLastName = '';
    inputUserName = '';
    inputStreet = '';
    inputZip = '';
    inputCity = '';
  }

  $: {
    inputUserName =
      inputFirstName !== '' && inputLastName !== ''
        ? `${inputFirstName.toLowerCase()[0]}.${inputLastName.toLowerCase()}`
        : '';
  }

  $: {
    if (users) {
      filteredUsers = users.filter(u => {
        const term = [u.first_name, u.last_name]
          .join('')
          .toLowerCase()
          .trim();
        return term.includes(searchText.toLowerCase());
      });
    }
  }

  $: isInputFirstNameValid =
    inputFirstName.trim() !== '' && inputFirstName.length;
  $: isInputLastNameValid = inputLastName.trim() !== '';
  $: isInputUserNameValid =
    inputUserName.trim() !== '' && inputUserName.length > 5;
  $: isInputStreetValid = inputUserName.trim() !== '' && inputStreet.length > 3;
  $: isInputCityValid = inputCity.trim() !== '' && inputCity.length > 2;
  $: isInputZipValid =
    inputZip.trim() !== '' &&
    inputZip.length > 3 &&
    inputZip.length <= 12 &&
    inputZip.match(/^[0-9]+$/);
  $: isUserFormValid =
    isInputFirstNameValid &&
    isInputLastNameValid &&
    isInputUserNameValid & isInputStreetValid &&
    isInputCityValid &&
    isInputZipValid;
</script>

<div class="widget">
  <p class="widget-title">User Administration</p>
  <div class="widget-content">

    <div class="widget-column-half">
      {#if filteredUsers}
        <h3>Available Users</h3>
        <input
          class="input"
          bind:value={searchText}
          type="text"
          placeholder="Filter" />
        <ul class="list-box">
          {#each filteredUsers as u, userListIndex}
            <li
              on:click={() => (selectedUser = u)}
              class:selected-list-item={u === selectedUser}
              key={u.id}>
              {u.first_name} {u.last_name}
            </li>
          {/each}
        </ul>
        {#if selectedUser}
          <div class="user-info-box">
            <h3 class="text-white">User Info</h3>
            <p>Name: {selectedUser.first_name} {selectedUser.last_name}</p>
            <p>Username: {selectedUser.user_name}</p>
            <p>
              Address: {selectedUser.street}, {selectedUser.zip} {selectedUser.city}
            </p>
          </div>
        {/if}
      {/if}

    </div>

    <div class="widget-column-half">
      <form action="submit">
        <h3>Add User</h3>
        <label class="input-label" for="firstName">First Name</label>
        <input
          class="input"
          class:invalid={!isInputFirstNameValid}
          id="firstName"
          bind:value={inputFirstName}
          type="text"
          placeholder="First Name" />
        <br />

        <label class="input-label" for="lastName">Last Name</label>
        <input
          class="input"
          class:invalid={!isInputLastNameValid}
          id="lastName"
          bind:value={inputLastName}
          type="text"
          placeholder="Last Name" />
        <br />

        <label class="input-label" for="userName">Username</label>
        <input
          class="input"
          class:invalid={!isInputUserNameValid}
          id="userName"
          bind:value={inputUserName}
          type="text"
          placeholder={inputUserName} />
        <br />

        <hr />

        <label class="input-label" for="streetName">Street</label>
        <input
          class="input"
          class:invalid={!isInputStreetValid}
          id="streetName"
          bind:value={inputStreet}
          type="text"
          placeholder="Street" />
        <br />

        <label class="input-label" for="cityName">City</label>
        <input
          class="input"
          class:invalid={!isInputCityValid}
          id="cityName"
          bind:value={inputCity}
          type="text"
          placeholder="City" />
        <br />

        <label class="input-label" for="zipCode">Zip Code (numbers only)</label>
        <input
          class="input"
          class:invalid={!isInputZipValid}
          id="zipCode"
          bind:value={inputZip}
          type="text"
          placeholder="Zip Code" />
        <br />
      </form>

      <button class="button" on:click={postUser} disabled={!isUserFormValid}>
        POST USER
      </button>
    </div>

  </div>
</div>
