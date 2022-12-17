import { TState } from './common'

export interface TAttemptInput {
	attempt: string
}

export interface TAttemptResponse {
	attempt: string
	letters_status: number[]
}

export enum AttemptLetterStatus {
	Incorrect = 0,
	Included = 1,
	Correct = 2,
}

export type TAttemptState = TState<TAttemptResponse, any>
