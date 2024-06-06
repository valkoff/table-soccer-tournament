<script lang="ts">
	import { onMount } from 'svelte';
	import { players } from '../../stores/playerStore';
	import { getPlayers, type Player, type Match } from '$lib/api';
	import PlayerSelect from '../../components/PlayerSelect.svelte';

	let newMatch: Match = {
		id: 0,
		date: new Date(),
		teamA: [],
		teamB: [],
		scoreA: 0,
		scoreB: 0
	};

	let newMatchDate = '';

	onMount(async () => {
		const fetchedPlayers = await getPlayers();
		players.set(fetchedPlayers);
	});

	async function handleAddMatch() {
		console.log('newMatch', newMatch);
	}

	function handleTeamPlayerA(event: CustomEvent<Player>) {
		newMatch.teamA.push(event.detail);
	}
	function handleTeamPlayerB(event: CustomEvent<Player>) {
		newMatch.teamB.push(event.detail);
	}
</script>

<div class="p-4">
	<h1 class="text-2xl font-bold mb-4">Matches</h1>

	<form>
		<div class="space-y-12">
			<div class="border-b border-gray-900/10 pb-12">
				<h2 class="text-base font-semibold leading-7 text-gray-900">Create Match</h2>

				<div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
					<div class="sm:col-span-4">
						<label for="username" class="block text-sm font-medium leading-6 text-gray-900"
							>Date</label
						>
						<div class="mt-2">
							<div
								class="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md"
							>
								<input
									type="text"
									bind:value={newMatchDate}
									name="username"
									id="username"
									autocomplete="username"
									class="block flex-1 border-0 bg-transparent py-1.5 pl-1 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6"
								/>
							</div>
						</div>
					</div>
				</div>

				<div class="mt-10 columns-2">
					<div>
						<h4>Team A</h4>
						<div class="columns-2">
							<div>
								<PlayerSelect players={$players} on:select={handleTeamPlayerA} />
							</div>
							<div>
								<PlayerSelect players={$players} on:select={handleTeamPlayerA} />
							</div>
						</div>
					</div>
					<div>
						<h4>Team B</h4>
						<div class="columns-2">
							<div>
								<PlayerSelect players={$players} on:select={handleTeamPlayerB} />
							</div>
							<div>
								<PlayerSelect players={$players} on:select={handleTeamPlayerB} />
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="mt-6 flex items-center justify-end gap-x-6">
				<button type="button" class="text-sm font-semibold leading-6 text-gray-900">Cancel</button>
				<button
					on:click={handleAddMatch}
					class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
					>Save</button
				>
			</div>
		</div>
	</form>
</div>
