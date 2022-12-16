import { TState } from './common'

export interface TSessionResponse {
	access_token: string
	token_type: string
}

export interface TSessionInput {
	username: string
	password: string
	grant_type: string
}

export type TSessionState = TState<TSessionResponse, any>
