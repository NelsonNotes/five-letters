import { TSessionInput, TSessionResponse } from '../types/session'
import { customFetch } from './utils'

// A mock function to mimic making an async request for data
export const sessionAPI = {
	getSession: (credentials: TSessionInput): Promise<TSessionResponse> =>
		customFetch('/login/access-token', 'POST', credentials, true),
}
