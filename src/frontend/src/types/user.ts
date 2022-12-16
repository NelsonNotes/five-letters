import { TAttemptResponse } from './attempt'
import { TState } from './common'

export interface TUserResponse {
	first_name: string
	last_name: string
	email: string
	avatar_url?: string
	current_word_id: number
	attempts: TAttemptResponse[]
}

export type TUserState = TState<TUserResponse, any>
