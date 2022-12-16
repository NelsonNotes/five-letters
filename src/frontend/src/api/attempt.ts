import { TAttemptInput, TAttemptResponse } from '../types/attempt'
import { customFetch } from './utils'

// A mock function to mimic making an async request for data
export const attemptAPI = {
	postAttempt: (attempt: TAttemptInput): Promise<TAttemptResponse> =>
		customFetch('/attempt/', 'POST', attempt),
}
