import type { Player } from "$lib/api";
import { writable } from "svelte/store";

export const players = writable(<Player[]>[]);
