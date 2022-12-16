import { TSessionInput, TSessionResponse } from '../types/session'

// A mock function to mimic making an async request for data
export const sessionAPI = {
	getSession: (credentials: TSessionInput) => {
		return new Promise<TSessionResponse>((resolve) =>
			setTimeout(
				() =>
					resolve({
						access_token: 'fakeBearerTokenString',
						token_type: 'Bearer',
					}),
				500
			)
		)
	},
}
